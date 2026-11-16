"""Porównanie wag i dwóch sposobów uśredniania cen i płac w polskich umowach."""
from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, fields
from pathlib import Path
from statistics import median

from walidacja_pl import (
    CPI, HORIZONS, RATE, RESERVE, Result, build_wage, compare, factors, pct, pln, table,
)

# GUS, Budżety gospodarstw domowych w 2024 r., wykres 1, s. 26.
# Obie części szeregu mają różne podstawy uogólniania wyników.
HOUSEHOLD_INCOME = {
    2011: 1235, 2012: 1278, 2013: 1299, 2014: 1340, 2015: 1386,
    2016: 1475, 2017: 1598, 2018: 1693, 2019: 1819, 2020: 1919,
    2021: 2103, 2022: 2355, 2023: 2678, 2024: 3167,
}
HOUSEHOLD_BLOCKS = ((2011, 2020), (2021, 2024))
SCHEDULES = (("Faktura", "odroczona", 0.0), ("Raty 0%", "raty", 0.0),
             ("Raty 5%", "raty", RATE))
SCENARIOS = (
    ("Bazowy", 1.0, 1.0, RESERVE),
    ("Dochód −25%", 0.75, 1.0, RESERVE),
    ("Koszty +20%", 1.0, 1.20, RESERVE),
    ("Oba szoki, rezerwa 5%", 0.75, 1.20, RESERVE),
    ("Oba szoki, rezerwa 15%", 0.75, 1.20, 0.15),
)


def alternatives(price: float, wage: float) -> dict[str, float]:
    return {
        **factors(price, wage),
        "Arytmetyczna 50/50": (price + wage) / 2,
        "Geometryczna 25/75": price**0.25 * wage**0.75,
        "Geometryczna 75/25": price**0.75 * wage**0.25,
    }


def contracts(blocks: tuple[tuple[int, int], ...]) -> list[tuple[int, int]]:
    return [
        (start, start + horizon)
        for first, last in blocks
        for horizon in HORIZONS
        for start in range(first, last - horizon + 1)
    ]


def comparisons() -> list[tuple[str, str, Result]]:
    wage = build_wage()
    matched = contracts(HOUSEHOLD_BLOCKS)
    samples = (
        ("Płace, pełna historia", contracts(((min(CPI), max(CPI)),)), None),
        ("Płace, okna GUS", matched, None),
        ("Dochód GUS, te same okna", matched, HOUSEHOLD_INCOME),
    )
    return [
        (sample, label, result)
        for sample, windows, income_series in samples
        for label, schedule, rate in SCHEDULES
        for start, end in windows
        for scenario, income, costs, reserve in SCENARIOS
        for result in compare(
            start, end, wage, schedule, rate, scenario=scenario, income_factor=income,
            cost_factor=costs, reserve=reserve, factor_rule=alternatives, income_series=income_series,
        )
    ]


def summary(rows: list[tuple[str, str, Result]]) -> None:
    groups: dict[tuple[str, str, str, str], list[Result]] = {}
    for sample, schedule, result in rows:
        key = (sample, schedule, result.scenario, result.method)
        groups.setdefault(key, []).append(result)

    for sample in dict.fromkeys(key[0] for key in groups):
        print(f"## {sample}\n")
        table(
            ("Umowa", "Metoda", "Okna", "Mediana obciążenia", "Szczyt obciążenia",
             "Mediana wartości realnej wpływów / baza", "Najgorszy ubytek realny",
             "Luka D / W · % okien", "Największa luka D / W · zł", "Maks. żal"),
            (
                (schedule, method, len(base),
                 pct(median(r.peak_payment_share for r in base)),
                 pct(max(r.peak_payment_share for r in base)),
                 pct(median(1 - r.real_loss for r in base)),
                 pct(max(r.real_loss for r in base)),
                 gap_frequency(base), gap_maximum(base), pct(max(r.regret for r in base)))
                for (group, schedule, scenario, method), base in groups.items()
                if group == sample and scenario == "Bazowy"
            ),
        )
        table(
            ("Umowa", "Scenariusz", "Metoda", "Luka D / W · % okien",
             "Największa luka D / W · zł", "Największa luka którejkolwiek strony · zł"),
            (
                (schedule, scenario, method, gap_frequency(stress), gap_maximum(stress),
                 pln(max(max(r.debtor_gap_real, r.creditor_gap_real) for r in stress)))
                for (group, schedule, scenario, method), stress in groups.items()
                if group == sample and scenario != "Bazowy"
            ),
        )

    print("## Zmiana zakresu · oba szoki, rezerwa 5%\n")
    restricted = []
    for (sample, schedule, scenario, method), results in groups.items():
        if sample != "Płace, pełna historia" or scenario != "Oba szoki, rezerwa 5%":
            continue
        for horizon in (1, 5):
            subset = [r for r in results if r.start >= 1999 and r.end - r.start >= horizon]
            largest_gap = max(max(r.debtor_gap_real, r.creditor_gap_real) for r in subset)
            restricted.append((schedule, 1999, horizon, method, len(subset), pln(largest_gap)))
    table(
        ("Umowa", "Początek najwcześniej", "Min. horyzont", "Metoda", "Okna",
         "Największa luka którejkolwiek strony · zł"),
        restricted,
    )


def gap_frequency(sample: list[Result]) -> str:
    debtor = sum(r.debtor_gap_real > 1e-7 for r in sample) / len(sample)
    creditor = sum(r.creditor_gap_real > 1e-7 for r in sample) / len(sample)
    return f"{pct(debtor)} / {pct(creditor)}"


def gap_maximum(sample: list[Result]) -> str:
    return (f"{pln(max(r.debtor_gap_real for r in sample))} / "
            f"{pln(max(r.creditor_gap_real for r in sample))}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, help="Nowy plik ze szczegółowymi wynikami.")
    args = parser.parse_args()
    rows = comparisons()
    if args.csv:
        with args.csv.open("x", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=[
                "sample", "contract", *(f.name for f in fields(Result)), "regret",
            ])
            writer.writeheader()
            writer.writerows(
                {"sample": sample, "contract": contract, **asdict(result), "regret": result.regret}
                for sample, contract, result in rows
            )
    summary(rows)


if __name__ == "__main__":
    main()
