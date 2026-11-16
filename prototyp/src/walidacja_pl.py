"""Porównanie czterech metod rozliczeń. Czyta historię bez jej aktualizacji."""
from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, dataclass, fields
from datetime import date
from itertools import pairwise
import json
from math import sqrt
from pathlib import Path
from statistics import median
import subprocess
from typing import Callable, Iterable

from regret_poland import CHAIN_1999, CPI, build_wage

ROOT = Path(__file__).resolve().parents[2]
METHODS = ("Nominał", "CPI", "Płace", "Talent")
PRINCIPAL = 100_000
STARTING_INCOME = 100_000
HORIZONS = range(1, 31)
RATE = 0.05
FUNDING_SHARE = 0.25
LENDER_OUTFLOW = 0.90
RESERVE = 0.05
EXAMPLES = {
    (1989, 1994): "Transformacja",
    (1999, 2004): "Spadek inflacji",
    (2009, 2014): "Okno porównawcze",
    (2014, 2019): "Deflacja, potem wzrost cen",
    (2019, 2024): "Pandemia i inflacja",
}


@dataclass(frozen=True)
class Result:
    start: int
    end: int
    schedule: str
    scenario: str
    interest: float
    method: str
    payments_pln: float
    regret_debtor: float
    regret_creditor: float
    real_loss: float
    peak_payment_share: float
    first_payment_increase: float
    max_payment_increase: float | None
    debtor_gap_real: float
    creditor_gap_real: float

    @property
    def regret(self) -> float:
        return max(self.regret_debtor, self.regret_creditor)


def factors(price: float, wage: float) -> dict[str, float]:
    return dict(zip(METHODS, (1.0, price, wage, sqrt(price * wage)), strict=True))


def schedule_terms(start: int, end: int, schedule: str, interest: float) -> list[tuple[int, float]]:
    if schedule == "odroczona":
        return [(end, PRINCIPAL)]
    periods = end - start
    amortization = PRINCIPAL / periods
    return [
        (start + period, amortization + interest * (PRINCIPAL - (period - 1) * amortization))
        for period in range(1, periods + 1)
    ]


def funding_gap(flows: Iterable[float], reserve: float) -> float:
    """Minimum dodatkowych środków przy założeniu zachowania nadwyżek."""
    lowest_balance = 0.0
    balance = reserve
    for flow in flows:
        balance += flow
        lowest_balance = min(lowest_balance, balance)
    return abs(lowest_balance)


def compare(
    start: int,
    end: int,
    wage: dict[int, float],
    schedule: str,
    interest: float,
    *,
    scenario: str = "bazowy",
    income_factor: float = 1.0,
    cost_factor: float = 1.0,
    reserve: float = RESERVE,
    factor_rule: Callable[[float, float], dict[str, float]] = factors,
    income_series: dict[int, float] | None = None,
) -> list[Result]:
    terms = schedule_terms(start, end, schedule, interest)
    prices = [CPI[year] / CPI[start] for year, _ in terms]
    wages = [wage[year] / wage[start] for year, _ in terms]
    bases = [base for _, base in terms]
    total_base = sum(bases)
    income_growth = wages if income_series is None else [
        income_series[year] / income_series[start] for year, _ in terms
    ]
    resources = [STARTING_INCOME * growth * income_factor for growth in income_growth]
    # Faktura jest płatna z kwoty odłożonej już na dzień zapłaty.
    share = FUNDING_SHARE if schedule == "raty" else 1.0
    start_reserve = PRINCIPAL * reserve
    result = []
    candidates = [factor_rule(c, w) for c, w in zip(prices, wages, strict=True)]

    for method in candidates[0]:
        multipliers = [candidate[method] for candidate in candidates]
        payments = [base * m for base, m in zip(bases, multipliers, strict=True)]
        real_payments = [payment / c for payment, c in zip(payments, prices, strict=True)]
        payments_in_raise = [current / previous - 1 for previous, current in pairwise(payments)]
        debtor_flow = (
            (balance * share - payment) / c
            for balance, payment, c in zip(resources, payments, prices, strict=True)
        )
        creditor_flow = (
            payment - LENDER_OUTFLOW * base * cost_factor
            for payment, base in zip(real_payments, bases, strict=True)
        )
        result.append(Result(
            start=start, end=end, schedule=schedule, scenario=scenario, interest=interest,
            method=method, payments_pln=sum(payments),
            regret_debtor=max(0.0, *(r / w - 1 for r, w in zip(multipliers, wages, strict=True))),
            regret_creditor=max(0.0, *(c / r - 1 for c, r in zip(prices, multipliers, strict=True))),
            real_loss=1 - sum(real_payments) / total_base,
            peak_payment_share=max(p / y for p, y in zip(payments, resources, strict=True)),
            first_payment_increase=multipliers[0] - 1,
            max_payment_increase=max(0, *payments_in_raise) if payments_in_raise else None,
            debtor_gap_real=funding_gap(debtor_flow, start_reserve),
            creditor_gap_real=funding_gap(creditor_flow, start_reserve),
        ))
    return result


def all_windows(wage: dict[int, float]) -> list[Result]:
    return [
        outcome
        for horizon in HORIZONS
        for start in range(min(CPI), max(CPI) - horizon + 1)
        for schedule, interest in (("odroczona", 0.0), ("raty", 0.0), ("raty", RATE))
        for outcome in compare(start, start + horizon, wage, schedule, interest)
    ]


def sensitivity(wage: dict[int, float]) -> list[Result]:
    return [
        outcome
        for (start, end) in ((1989, 1994), (2009, 2014), (2019, 2024))
        for schedule, rate in (("raty", RATE), ("odroczona", 0))
        for name, income, cost, reserve in (
            ("bazowy", 1.0, 1.0, RESERVE),
            ("dochód −25%", 0.75, 1.0, RESERVE),
            ("koszty +20%", 1.0, 1.20, RESERVE),
            ("oba szoki, rezerwa 5%", 0.75, 1.20, RESERVE),
            ("oba szoki, rezerwa 15%", 0.75, 1.20, 0.15),
        )
        for outcome in compare(start, end, wage, schedule, rate,
                               scenario=name, income_factor=income, cost_factor=cost, reserve=reserve)
    ]


def pct(value: float) -> str:
    return f"{round(100 * value, 2) + 0.0:.2f}%".replace(".", ",")


def pln(value: float) -> str:
    return f"{round(value, 2) + 0.0:,.2f}".replace(",", " ").replace(".", ",")


def table(headers: tuple[str, ...], rows: Iterable[Iterable[object]]) -> None:
    print("| " + " | ".join(headers) + " |")
    print("| " + " | ".join("---" for _ in headers) + " |")
    for row in rows:
        print("| " + " | ".join(map(str, row)) + " |")
    print()


def metrics_rows(grid: list[Result]) -> Iterable[tuple]:
    for schedule, rate in (("odroczona", 0.0), ("raty", 0.0), ("raty", RATE)):
        for method in METHODS:
            sample = [r for r in grid if (r.schedule, r.interest, r.method) == (schedule, rate, method)]
            worst = max(sample, key=lambda r: r.regret)
            increases = [r.max_payment_increase for r in sample if r.max_payment_increase is not None]
            yield (
                schedule, pct(rate), method, pct(median(r.regret for r in sample)),
                f"{pct(worst.regret)} ({worst.start}–{worst.end})",
                pct(median(r.real_loss for r in sample)),
                pct(max(r.peak_payment_share for r in sample)),
                pct(max(r.first_payment_increase for r in sample)),
                pct(max(increases)) if increases else "—",
                pct(sum(r.debtor_gap_real > 1e-7 for r in sample) / len(sample)),
                pct(sum(r.creditor_gap_real > 1e-7 for r in sample) / len(sample)),
            )


def vintage_tables() -> None:
    data = json.loads((ROOT / "prototyp/data/manual/walidacja_cpi_2026.json").read_bytes())
    path = "prototyp/data/processed/talent_anchors.csv"
    archive = subprocess.check_output(
        ["git", "show", f"{data['published_revision']}:{path}"], cwd=ROOT, text=True
    )
    history = {r[""]: r for r in csv.DictReader(archive.splitlines())}
    reference = history["2026-05"]
    targets = sorted(data["cpi"])
    totals = {version: dict.fromkeys(METHODS, 0.0)
              for version in ("opublikowane", "odczyty znane przed odcięciem", "tabela listopadowa")}
    regular = revised = 1.0
    rates = []
    installment = 2500
    previous_price = float(reference["I_c"])

    for month in targets:
        year, month_index = map(int, month.split("-"))
        cycle_year = year + (month_index == 12)
        cycle_month = month_index % 12 + 1
        cutoff = date(cycle_year, cycle_month, 24)
        observation = data["cpi"][month]
        release = date.fromisoformat(observation["regular_release_date"])
        if release >= cutoff:
            raise ValueError(f"Brak udokumentowanego CPI sprzed odcięcia dla {month}.")
        regular *= observation["regular_rate"] / 100
        revised *= observation["november_table_rate"] / 100
        price = float(history[month]["I_c"])
        applied_rate = round(100 * price / previous_price, 1)
        previous_price = price
        wage = float(history[month]["I_w"]) / float(reference["I_w"])
        published = factors(price / float(reference["I_c"]), wage)
        published["Talent"] = float(history[month]["A"]) / float(reference["A"])
        before_cutoff = factors(regular, wage)
        later = factors(revised, wage)
        for version, multipliers in zip(totals, (published, before_cutoff, later), strict=True):
            for method, factor in multipliers.items():
                totals[version][method] += installment * factor
        rates.append((
            month, f"[{release.isoformat()}]({observation['source']})", cutoff.isoformat(),
            pln(applied_rate), pln(observation["regular_rate"]), pln(observation["november_table_rate"]),
            pln(installment * published["Talent"]), pln(installment * before_cutoff["Talent"]),
        ))

    table(("Miesiąc", "Regularny komunikat GUS", "Dzień odcięcia", "CPI użyty",
           "CPI przed odcięciem", "CPI w listopadzie", "Rata TLN z publikacji (zł)",
           "Rata TLN z CPI dostępnego przed odcięciem (zł)"), rates)
    table(("Wejścia", *METHODS), ((version, *(pln(value) for value in sums.values()))
                                for version, sums in totals.items()))


def report_tables(wage: dict[int, float], grid: list[Result], stressed: list[Result]) -> None:
    print("## Wyniki łączne · wszystkie roczniki i horyzonty 1–30 lat\n")
    table(("Umowa", "Oprocentowanie", "Metoda", "Mediana żalu", "Maks. żal",
           "Mediana realnego ubytku", "Szczyt obciążenia", "Maks. wzrost pierwszej płatności",
           "Maks. podwyżka między ratami", "Luka dłużnika, odsetek okien",
           "Luka wierzyciela, odsetek okien"), metrics_rows(grid))

    print("## Zmiana zakresu próby · Talent\n")
    rows = []
    for first_year, lengths, label in (
        (1989, (3, 5, 10, 20, 30), "Pięć horyzontów z dawnego raportu"),
        (1989, range(3, 31), "Wszystkie horyzonty 3–30"),
        (1989, HORIZONS, "Wszystkie horyzonty 1–30"),
        (1999, HORIZONS, "Roczniki startu od 1999"),
    ):
        sample = [r for r in grid if r.method == "Talent" and r.interest == 0
                  and r.start >= first_year and r.end - r.start in lengths]
        deferred = [r for r in sample if r.schedule == "odroczona"]
        worst_once = max(deferred, key=lambda r: r.regret)
        worst_loan = max((r for r in sample if r.schedule == "raty"), key=lambda r: r.regret)
        rows.append((
            label, len(deferred),
            f"{pct(worst_once.regret)} ({worst_once.start}–{worst_once.end})",
            f"{pct(worst_loan.regret)} ({worst_loan.start}–{worst_loan.end})",
        ))
    table(("Zakres", "Okna na wariant", "Najgorszy żal · jedna płatność",
           "Najgorszy żal · raty"), rows)

    print("## Horyzonty · maksymalny żal we wszystkich rocznikach\n")
    table(("Lata", "Roczniki startu", "Okna", *(
        f"{method} · {schedule}" for schedule in ("odroczona", "raty") for method in METHODS
    )), (
        (horizon, f"{min(CPI)}–{max(CPI) - horizon}", max(CPI) - min(CPI) + 1 - horizon,
         *(pct(max(r.regret for r in grid if r.end - r.start == horizon and r.schedule == schedule
                   and r.method == method and r.interest == 0))
           for schedule in ("odroczona", "raty") for method in METHODS))
        for horizon in HORIZONS
    ))

    print("## Przykłady · faktura z rocznym odroczeniem, bez odsetek\n")
    table(("Okno", "Metoda", "Płatność (zł)", "Żal D", "Żal W", "Ubytek realny sprzedawcy",
           "Płatność / budżet kupującego", "Luka kupującego (zł realne)",
           "Luka sprzedawcy (zł realne)"), (
        (f"{r.start}–{r.end}", r.method, pln(r.payments_pln), pct(r.regret_debtor),
         pct(r.regret_creditor), pct(r.real_loss), pct(r.peak_payment_share),
         pln(r.debtor_gap_real), pln(r.creditor_gap_real))
        for r in grid if (r.start, r.end) in ((2014, 2015), (2021, 2022))
        and r.schedule == "odroczona"
    ))

    print("## Przykłady · raty, 5%\n")
    table(("Okno", "Metoda", "Suma nominalna (zł)", "Żal D", "Żal W", "Ubytek realny wierzyciela",
           "Najwyższa rata / dochód", "Wzrost pierwszej raty", "Wzrost między ratami",
           "Luka D (zł realne)", "Luka W (zł realne)"), (
        (f"{EXAMPLES[(r.start, r.end)]} ({r.start}–{r.end})", r.method, pln(r.payments_pln),
         pct(r.regret_debtor), pct(r.regret_creditor), pct(r.real_loss), pct(r.peak_payment_share),
         pct(r.first_payment_increase), pct(r.max_payment_increase),
         pln(r.debtor_gap_real), pln(r.creditor_gap_real))
        for r in grid if (r.start, r.end) in EXAMPLES and r.schedule == "raty" and r.interest == RATE
    ))

    print("## Wrażliwość · luka dłużnika / wierzyciela w realnych PLN\n")
    def gap_pair(r):
        return f"{pln(r.debtor_gap_real)} / {pln(r.creditor_gap_real)}"
    table(("Okno", "Umowa", "Scenariusz", *METHODS), (
        (f"{r.start}–{r.end}", r.schedule, r.scenario, *(gap_pair(item) for item in stressed[i:i+4]))
        for i, r in enumerate(stressed) if i % len(METHODS) == 0
    ))

    print("## Warianty łączenia serii w 1999 r.\n")
    rows = []
    for connection in (1.05, CHAIN_1999, 1.20):
        adjusted = {year: value * connection / CHAIN_1999 if year >= 1999 else value
                    for year, value in wage.items()}
        sample = grid if connection == CHAIN_1999 else all_windows(adjusted)
        crossing = [r for r in sample if r.start < 1999 <= r.end and r.method == "Talent"]
        rows.append((
            pct(connection - 1),
            pct(max(r.regret for r in crossing if r.schedule == "odroczona")),
            pct(max(r.regret for r in crossing if r.schedule == "raty")),
            pct(median(r.real_loss for r in crossing if r.schedule == "odroczona")),
        ))
    table(("Łącznik", "Maks. żal kwoty odroczonej", "Maks. żal rat", "Mediana ubytku wierzyciela dla płatności odroczonej"), rows)

    print("## Publikacje 2026 · odczyt przed odcięciem, odczyt użyty i późniejsza tabela\n")
    vintage_tables()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, help="Nowy plik ze wszystkimi wynikami rocznymi.")
    args = parser.parse_args()
    wage = build_wage()
    grid = all_windows(wage)
    stressed = sensitivity(wage)
    if args.csv:
        with args.csv.open("x", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=[f.name for f in fields(Result)] + ["regret"])
            writer.writeheader()
            writer.writerows({**asdict(r), "regret": r.regret} for r in grid + stressed)
    report_tables(wage, grid, stressed)


if __name__ == "__main__":
    main()
