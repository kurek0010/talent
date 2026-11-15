# Prototyp obliczeniowy Talenta

Kod referencyjny liczący jednostkę **Talent (TLN)** — środek geometryczny indeksu cen i indeksu płac, √(C×W) — oraz przeprowadzający testy historyczne (minimax regret) i budujący stronę.

Zasada projektu: **kod jest metodologią**. Możliwość odtworzenia wyniku zależy od dostępności tej samej wersji kodu i wejść. Archiwalne testy AUV mają niepełne wejścia.

## Wymagania

- Python 3.10 lub nowszy
- Klucz FRED tylko do ponownego pobierania z FRED. Builder i testy wykorzystujące zapisane wejścia działają bez klucza.

## Setup

```bash
# w katalogu prototyp/
python3 -m venv .venv
source .venv/bin/activate     # macOS/Linux
pip install -r requirements.txt

```

Dane wejściowe są dołączone w `data/` (surowe pobrania + przetworzone wyniki), więc skrypty analiz i builder działają bez ponownego pobierania.

## Polecenia

Do testów zapisujących wyniki używaj odrębnej kopii repozytorium. `talent_daily.py` zapisuje demonstrację w `data/research/`. Kod prospektywnej próby i sposób odtworzenia opisuje [instrukcja aktualizacji](../INSTRUKCJA_aktualizacji.md#próba-prospektywna-tip-0003).

```bash
python src/talent_daily.py     # kotwice miesięczne + ścieżka dzienna Talenta
python src/regret_century.py   # próby USA na CPI i PKB/os. (od 1929) oraz CPI i płacach (od 1939)
python src/regret_poland.py    # Polska 1989–2024
python src/regret_bilateral.py # jednostka dwustronna PL–US
python src/build_strona.py     # przebudowa wszystkich plików HTML w korzeniu repo
```

Cykl miesięczny obejmuje pobranie wejść, dopisanie kotwicy, uzupełnienie przeliczeń walutowych i przebudowę strony. [Instrukcja aktualizacji](../INSTRUKCJA_aktualizacji.md)

## Kalkulator waloryzacji

[Demonstrator](../index.html#waloryzacja) mapuje każdą datę na jej miesiąc kalendarzowy. Korzysta z poziomu CPI z `talent_anchors.csv` i kotwicy TLN z `talent_anchors.json`. Builder przekazuje odczyty do 0,001 pkt. Kwotę obliczamy jako kwotę bazową razy iloraz odczytów końcowego i początkowego. Każdą należność zaokrąglamy do grosza, z połówkami w górę. Dla odczytów z tego samego miesiąca mnożnik wynosi 1. Brak któregoś odczytu wstrzymuje obliczenie. Odczyt za dany miesiąc mógł zostać ogłoszony po dacie podanej w formularzu.

| Przykład | Kwota nominalna | CPI | Talent |
|---|---:|---:|---:|
| Faktura za 100 000 zł, XII 2021 → XII 2022 | 100 000,00 zł | 116 814,92 zł | 114 275,61 zł |
| Pożyczka 10 000 zł, V → IX 2026, jedna płatność | 10 000,00 zł | 9 969,99 zł | 10 032,00 zł |
| Ta sama pożyczka, cztery raty po 2 500 zł bazowo, VI–IX 2026 | 10 000,00 zł | 9 970,00 zł | 10 026,12 zł |

Faktura ilustruje epizod 2021–2022 z raportu etapu 3. W raporcie są średnie roczne, a demonstrator używa odczytów grudniowych. Różnica jednego grosza między sumami CPI dla pożyczki w raporcie i demonstratorze wynika z odrębnego zaokrąglenia każdej należności w demonstratorze. Oba przykłady przyjmują zero odsetek i opłat. [Raport porównawczy](../materialy/walidacja_talent_pl.md)

Przebuduj HTML i uruchom `node --test prototyp/tests/test_kalkulator_umowy.cjs` z katalogu głównego repozytorium.

## Struktura

```
prototyp/
├── README.md              ← ten plik
├── requirements.txt
├── .env.example           (skopiuj do .env — Twój klucz FRED, gitignored)
│
├── src/
│   ├── talent_daily.py    kotwice miesięczne + ścieżka dzienna
│   ├── talent_update.py   dołożenie nowej kotwicy (aktualizacja miesięczna)
│   ├── fetch_gus.py       pobranie dynamik CPI GUS i próba uzupełnienia płac rocznych
│   ├── regret_century.py  test USA 1929–2025 (minimax regret)
│   ├── regret_poland.py   test Polska 1989–2024
│   ├── regret_bilateral.py jednostka dwustronna (PL–US)
│   ├── backtest_1900.py   test wsteczny na długiej serii
│   ├── build_strona.py    builder generowanych stron HTML w korzeniu repo
│   ├── strona_szablon.html szablon strony głównej
│   ├── config.py          rejestr publicznych serii danych
│   ├── download.py        orkiestracja pobierania
│   ├── harmonize.py       ujednolicenie częstotliwości i okresów
│   └── sources/           adaptery: FRED, NBP, ECB, World Bank, Yahoo, manual
│
└── data/
    ├── raw/               surowe pobrania (dokumentacyjne — patrz POLITYKA_danych)
    ├── manual/            ręcznie wprowadzone serie (backtest historyczny)
    └── processed/         daily.parquet, monthly.parquet, talent_* , regret_*
```

## Dane

Repozytorium zawiera publiczne migawki i szeregi wpisane ręcznie. Poziomy płac w polskim teście zweryfikowano w GUS. Przybliżony łącznik 1999 r. wymaga potwierdzenia. Ścieżka miesięcznej publikacji, demonstracja dzienna i testy historyczne mają różne wejścia. [Polityka danych](../POLITYKA_danych_v0.1.md)

## Zmiany metodologii

Każda zmiana formuły, źródeł lub reguły publikacyjnej przechodzi przez proces **TIP** (`../TIP/README.md`): nazwij problem → zaproponuj → przetestuj na danych → dopiero zmień regułę, nigdy wstecz.
