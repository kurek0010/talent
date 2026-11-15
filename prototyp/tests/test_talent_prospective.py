from copy import deepcopy
from datetime import date, timedelta
from decimal import Decimal
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import talent_prospective as talent

SOURCE = "https://stat.gov.pl/test"
JAN = date(2028, 1, 25)
FEB = date(2028, 2, 25)
MAR = date(2028, 3, 25)


def inputs_for(issued, months=1, cpi="100"):
    def record(month, value):
        available = talent.month_offset(month, 1).isoformat()
        return {"value": value, "available_by": f"{available}T12:00:00+01:00", "source": SOURCE}

    return {
        "cpi": {
            month.strftime("%Y-%m"): record(month, cpi)
            for month in (talent.month_offset(issued, i) for i in range(-months, 0))
        },
        "wages": {
            month.strftime("%Y-%m"): record(month, "10000")
            for month in (talent.month_offset(issued, i) for i in range(-12, 0))
        },
    }


class ProspectiveTests(unittest.TestCase):
    def test_gus_inputs_and_base(self):
        fixture = Path(__file__).parent / "fixtures" / "tip0003-gus-2026-09.json"
        inputs = json.loads(fixture.read_bytes())
        result = talent.calculate(inputs, date(2026, 10, 25), None)
        self.assertAlmostEqual(float(result["base_wage"]), 9288.128333333333, places=9)
        self.assertEqual(set(result["daily"].values()), {"100.000000"})
        self.assertEqual(result["cutoff"], "2026-10-24T12:00:00+02:00")

    def test_daily_path_connects_two_anchors(self):
        first = talent.calculate(inputs_for(JAN), JAN, None)
        second = talent.calculate(inputs_for(FEB, cpi="121"), FEB, first)
        third = talent.calculate(inputs_for(MAR), MAR, second)

        self.assertEqual(first["daily"]["2028-02-25"], "100.000000")
        self.assertEqual(second["anchor"], "110.000000")
        self.assertEqual(second["daily"]["2028-03-25"], "110.000000")
        self.assertEqual(third["daily"]["2028-03-26"], "110.000000")
        self.assertEqual(len(second["daily"]), 29)
        increments = [Decimal(first["anchor"]), *map(Decimal, second["daily"].values())]
        multipliers = [b / a for a, b in zip(increments, increments[1:])]
        self.assertLess(max(multipliers) - min(multipliers), Decimal("0.00000002"))

    def test_missing_month_catches_up_without_backfill(self):
        first = talent.calculate(inputs_for(JAN), JAN, None)
        with self.assertRaisesRegex(ValueError, "2028-01"):
            talent.calculate(inputs_for(MAR), MAR, first)

        third = talent.calculate(inputs_for(MAR, months=2, cpi="110"), MAR, first)
        self.assertEqual(third["anchor"], "110.000000")
        dates = [date.fromisoformat(day) for day in third["daily"]]
        self.assertEqual(dates[0], MAR + timedelta(days=1))
        self.assertEqual(dates[-1], date(2028, 4, 25))

    def test_cutoff_uses_local_time(self):
        inputs = inputs_for(date(2026, 10, 25))
        inputs["cpi"]["2026-09"]["available_by"] = "2026-10-24T10:00:00+00:00"
        talent.calculate(inputs, date(2026, 10, 25), None)
        inputs["cpi"]["2026-09"]["available_by"] = "2026-10-24T10:00:01+00:00"
        with self.assertRaisesRegex(ValueError, "odcięcie"):
            talent.calculate(inputs, date(2026, 10, 25), None)

    def test_revisions_do_not_replace_archived_wages(self):
        first = talent.calculate(inputs_for(JAN), JAN, None)
        revised = inputs_for(FEB)
        revised["wages"]["2027-12"]["value"] = "9999"
        with self.assertRaisesRegex(ValueError, "Zmiana zarchiwizowanego"):
            talent.calculate(revised, FEB, first)

    def test_archive_replay_idempotence_and_tampering(self):
        with TemporaryDirectory() as tmp:
            folder = Path(tmp)
            inputs = inputs_for(JAN)
            first = talent.save_release(folder, JAN, inputs)
            saved = first.read_bytes()
            self.assertEqual(first, talent.save_release(folder, JAN, inputs))
            modified = deepcopy(inputs)
            modified["cpi"]["2027-12"]["value"] = "99"
            with self.assertRaisesRegex(ValueError, "ma już inne"):
                talent.save_release(folder, JAN, modified)

            second = talent.save_release(folder, FEB, inputs_for(FEB))
            self.assertEqual(len(talent.verified_releases(folder)), 2)
            self.assertEqual(first.read_bytes(), saved)
            first.unlink()
            with self.assertRaisesRegex(ValueError, "odtworzonym wynikiem"):
                talent.verified_releases(folder)
            first.write_bytes(saved)
            second.write_bytes(second.read_bytes().replace(b"100.000000", b"101.000000"))
            with self.assertRaisesRegex(ValueError, "odtworzonym wynikiem"):
                talent.verified_releases(folder)


if __name__ == "__main__":
    unittest.main()
