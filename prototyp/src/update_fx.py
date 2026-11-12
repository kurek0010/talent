"""Uzupełnia miesięczne przeliczenia TLN po ostatnim kursie tabeli A NBP."""

import csv
import json
from pathlib import Path

import pandas as pd

from sources.nbp import NBPSource

DATA = Path(__file__).resolve().parents[1] / "data" / "processed"
CURRENCIES = ("USD", "EUR", "CHF", "GBP", "CNY", "JPY")


def main() -> None:
    path = DATA / "talent_w_walutach.csv"
    with path.open(newline="") as handle:
        rows = list(csv.reader(handle))
    last_month = pd.Period(rows[-1][0], freq="M")
    published = json.loads((DATA / "talent_published.json").read_text())
    anchors = json.loads((DATA / "talent_anchors.json").read_text())
    months = pd.PeriodIndex(sorted(published), freq="M")
    months = months[months > last_month]
    if months.empty:
        print(f"Przeliczenia walut są aktualne do {last_month}.")
        return

    start = months[0].start_time.date().isoformat()
    end = months[-1].end_time.date().isoformat()
    source = NBPSource()
    rates = {}
    for currency in CURRENCIES:
        daily = source.get_exchange_rate(currency, start, end)
        monthly = daily.groupby(daily.index.to_period("M")).last().reindex(months)
        if monthly.isna().any() or (monthly <= 0).any():
            raise ValueError(f"Niepełne kursy NBP dla {currency} ({start}–{end})")
        rates[currency] = monthly

    new_rows = []
    for month in months:
        pln = anchors[str(month)] / 100
        new_rows.append([
            month.end_time.date().isoformat(),
            pln,
            *(pln / rates[currency].loc[month] for currency in CURRENCIES),
        ])
    updated = path.with_suffix(".tmp")
    with updated.open("w", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerows(rows)
        writer.writerows(new_rows)
    updated.replace(path)
    print(f"Dopisano {len(new_rows)} miesięcy przeliczeń NBP ({months[0]}–{months[-1]}).")


if __name__ == "__main__":
    main()
