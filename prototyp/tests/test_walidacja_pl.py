from math import isclose
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import walidacja_pl as model


class WalidacjaTests(unittest.TestCase):
    def test_equal_principal_and_common_interest(self):
        self.assertEqual(model.schedule_terms(2021, 2022, "odroczona", 0), [(2022, 100000)])
        self.assertEqual(model.schedule_terms(2019, 2024, "raty", 0), [
            (2020, 20000), (2021, 20000), (2022, 20000), (2023, 20000), (2024, 20000),
        ])
        self.assertEqual(model.schedule_terms(2019, 2024, "raty", 0.05), [
            (2020, 25000), (2021, 24000), (2022, 23000), (2023, 22000), (2024, 21000),
        ])

    def test_geometry_balances_ratios_but_not_ordinary_loss(self):
        payment = model.factors(1.5, 1.2)["Talent"]
        self.assertAlmostEqual(payment / 1.2 - 1, 1.5 / payment - 1)
        self.assertAlmostEqual(100 * (1 - payment / 1.5), 10.5572809000084)

    def test_funding_gap_from_worst_balance_not_final_balance(self):
        self.assertEqual(model.funding_gap([-10, -5, 30], 5), 10)
        self.assertEqual(model.funding_gap([-10, -5, 30], 15), 0)

    def test_all_vintages_and_base_metrics(self):
        grid = model.all_windows(model.build_wage())
        self.assertEqual(len(grid), 615 * 3 * 4)
        self.assertTrue(all(isclose(r.real_loss, 0, abs_tol=1e-14)
                            for r in grid if r.method == "CPI"))
        for horizon in range(1, 31):
            actual = {
                r.start for r in grid if r.end - r.start == horizon
                and r.schedule == "odroczona" and r.method == "Talent"
            }
            self.assertEqual(actual, set(range(1989, 2025 - horizon)))

        once, loan = (
            max(r.regret for r in grid if r.method == "Talent" and r.schedule == schedule
                and r.interest == 0 and r.end-r.start >= 3)
            for schedule in ("odroczona", "raty")
        )
        self.assertAlmostEqual(once, 0.10571719913015087)
        self.assertAlmostEqual(loan, 0.17432590382955127)

    def test_paying_capacity_is_separate_from_index(self):
        base, stress = (
            {r.method: r for r in model.compare(
                2019, 2024, model.build_wage(), "raty", 0.05,
                income_factor=income, cost_factor=cost
            )}
            for income, cost in ((1.0, 1.0), (0.75, 1.2))
        )
        for method in model.METHODS:
            self.assertEqual(base[method].payments_pln, stress[method].payments_pln)
            self.assertEqual(base[method].regret, stress[method].regret)
            self.assertGreaterEqual(stress[method].debtor_gap_real, base[method].debtor_gap_real)
            self.assertGreaterEqual(stress[method].creditor_gap_real, base[method].creditor_gap_real)
        self.assertGreater(stress["Talent"].debtor_gap_real, 0)
        self.assertGreater(stress["Talent"].creditor_gap_real, 0)


if __name__ == "__main__":
    unittest.main()
