"""Calculate and replay isolated TLN-PLN trial releases for TIP-0003."""
from __future__ import annotations

import argparse
from datetime import date, datetime, time, timedelta
from decimal import Decimal, DecimalException, ROUND_HALF_UP, localcontext
import fcntl
from hashlib import sha256
import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from urllib.parse import urlsplit
from zoneinfo import ZoneInfo

WARSAW = ZoneInfo("Europe/Warsaw")
VERSION = "TLN-PLN-TIP-0003-test"
CODE_SHA = sha256(Path(__file__).read_bytes()).hexdigest()
STORAGE = Path(__file__).resolve().parents[1] / "data" / "prospektywny-test"


def month_offset(day: date, offset: int) -> date:
    year, month = divmod(day.year * 12 + day.month - 1 + offset, 12)
    return date(year, month + 1, 1)


def canonical_json(value: dict) -> bytes:
    return (json.dumps(value, sort_keys=True, ensure_ascii=False, indent=2) + "\n").encode()


def observations(
    entries: dict, expected: list[date], cutoff: datetime, earlier: dict
) -> dict[str, Decimal]:
    months = {month.strftime("%Y-%m") for month in expected}
    if set(entries) != months:
        raise ValueError(
            f"Wejścia nie odpowiadają miesiącom. Brakuje: {sorted(months - entries.keys())}. "
            f"Nadmiarowe: {sorted(entries.keys() - months)}."
        )
    values = {}
    for month, record in sorted(entries.items()):
        value = Decimal(record["value"])
        source = urlsplit(record["source"])
        available = datetime.fromisoformat(record["available_by"])
        month_end = month_offset(date.fromisoformat(month + "-01"), 1)
        if not available.tzinfo or available.astimezone(WARSAW).date() < month_end:
            raise ValueError(f"Nieprawidłowa data dostępności za {month}.")
        if available > cutoff:
            raise ValueError(f"Odczyt za {month} jest późniejszy niż odcięcie.")
        if source.scheme != "https" or not (
            source.hostname == "stat.gov.pl" or (source.hostname or "").endswith(".stat.gov.pl")
        ):
            raise ValueError(f"Podaj adres publikacji GUS dla {month}.")
        if not isinstance(record["value"], str) or not value.is_finite() or value <= 0:
            raise ValueError(f"Podaj dodatnią wartość dziesiętną jako tekst dla {month}.")
        if month in earlier and record != earlier[month]:
            raise ValueError(f"Zmiana zarchiwizowanego wejścia za {month}.")
        values[month] = value
    return values


def calculate(inputs: dict, issued: date, previous: dict | None) -> dict:
    if issued.day != 25:
        raise ValueError("Cykl musi przypadać na 25. dzień miesiąca.")
    target = month_offset(issued, -1)
    start = issued + timedelta(days=1)
    end = month_offset(issued, 1).replace(day=25)
    cutoff = datetime.combine(issued.replace(day=24), time(12), WARSAW)
    cpi_months = [target]
    if previous:
        last = date.fromisoformat(previous["month"] + "-01")
        gap = (target.year - last.year) * 12 + target.month - last.month
        if gap <= 0:
            raise ValueError("Nowy cykl musi być późniejszy niż ostatni zapis.")
        cpi_months = [month_offset(last, offset) for offset in range(1, gap + 1)]

    cpi = observations(inputs["cpi"], cpi_months, cutoff, {})
    wages = observations(
        inputs["wages"], [month_offset(target, offset) for offset in range(-11, 1)],
        cutoff, previous["inputs"]["wages"] if previous else {},
    )

    with localcontext() as context:
        context.prec = 40
        context.rounding = ROUND_HALF_UP
        wage = sum(wages.values()) / 12
        price_index = Decimal(100)
        base_wage = wage
        if previous:
            base_wage = Decimal(previous["base_wage"])
            price_index = Decimal(previous["price_index"])
            for factor in cpi.values():
                price_index *= factor / 100

        anchor = (price_index * 100 * wage / base_wage).sqrt().quantize(Decimal("0.000001"))
        initial = Decimal(previous["anchor"]) if previous else anchor
        days = (end - start).days + 1
        step = (anchor / initial).ln()
        daily = {
            (start + timedelta(days=k - 1)).isoformat(): str(
                (initial * (step * k / days).exp()).quantize(Decimal("0.000001"))
            )
            for k in range(1, days + 1)
        }
        daily[end.isoformat()] = str(anchor)

    return {
        "version": VERSION,
        "code_sha256": CODE_SHA,
        "cycle_date": issued.isoformat(),
        "cutoff": cutoff.isoformat(),
        "month": target.strftime("%Y-%m"),
        "previous_sha256": sha256(canonical_json(previous)).hexdigest() if previous else None,
        "inputs_sha256": sha256(canonical_json(inputs)).hexdigest(),
        "inputs": inputs,
        "price_index": str(price_index),
        "base_wage": str(base_wage),
        "anchor": str(anchor),
        "daily": daily,
    }


def verified_releases(folder: Path) -> list[dict]:
    releases = []
    for path in sorted(folder.glob("????-??-??.json")):
        raw = path.read_bytes()
        record = json.loads(raw)
        replayed = calculate(
            record["inputs"], date.fromisoformat(path.stem), releases[-1] if releases else None
        )
        if canonical_json(replayed) != raw:
            raise ValueError(f"Archiwum nie zgadza się z odtworzonym wynikiem: {path}.")
        releases.append(record)
    return releases


def save_release(folder: Path, issued: date, inputs: dict) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / f"{issued}.json"
    with (folder / ".lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        releases = verified_releases(folder)
        if destination.exists():
            stored = json.loads(destination.read_bytes())
            if stored["inputs"] != inputs:
                raise ValueError(f"Cykl {issued} ma już inne zapisane wejścia.")
            return destination

        record = calculate(inputs, issued, releases[-1] if releases else None)
        with NamedTemporaryFile(dir=folder) as temp:
            temp.write(canonical_json(record))
            temp.flush()
            os.fsync(temp.fileno())
            os.link(temp.name, destination)
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    trial = commands.add_parser("test")
    trial.add_argument("inputs", type=Path)
    trial.add_argument("--cycle", required=True, type=date.fromisoformat)
    verify = commands.add_parser("verify")
    verify.add_argument("--expected-sha256", help="Niezależnie zapisany skrót ostatniego cyklu")
    args = parser.parse_args()

    try:
        if args.command == "test":
            print(save_release(STORAGE, args.cycle, json.loads(args.inputs.read_bytes())))
        else:
            releases = verified_releases(STORAGE)
            head = sha256(canonical_json(releases[-1])).hexdigest() if releases else None
            if args.expected_sha256 is not None and head != args.expected_sha256:
                raise ValueError("Skrót ostatniego cyklu nie zgadza się z oczekiwaną wartością.")
            print(f"Sprawdzone cykle testowe: {len(releases)}.")
            if head:
                print(f"SHA-256 ostatniego cyklu: {head}")
    except (DecimalException, KeyError, OSError, TypeError, ValueError) as error:
        parser.exit(1, f"Błąd: {error}\n")


if __name__ == "__main__":
    main()
