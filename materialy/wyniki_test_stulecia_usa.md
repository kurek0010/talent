# Test stulecia — zachowanie jednostki na danych USA 1929–2025

**Data:** 2026-07-04
**Kod:** `prototyp/src/regret_century.py` (odtwarzalny). Dane: FRED — CPI (CPIAUCNS, średnie roczne, od 1913), nominalny PKB na osobę (A939RC0A052NBEA, od 1929), płaca godzinowa produkcyjna w przemyśle (CES3000000008, od 1939); pobrane 2026-07-04, zapisane w `prototyp/data/raw/`. Wyniki: `prototyp/data/processed/regret_century.csv`.

**Korekta 2026-11-15.** Doprecyzowano zakres prób, jednostkę metryki i interpretację wyników. Tabele zachowują wartości z pierwotnego raportu.

**Status:** historyczne badanie porównawcze na danych USA. Skrypt bierze wszystkie dostępne lata startu dla horyzontów 3, 5, 10, 20 i 30 lat. Dla mnożników spłaty R, cen C i płac lub PKB na osobę W żal okna wynosi max(0, R/W − 1, C/R − 1). Skrypt liczy równoważną miarę logarytmiczną j i raportuje 100(eʲ − 1). „Zero-regret” oznacza j < 0,02, czyli poniżej około 2,02% w skali raportu. C/R − 1 różni się od zwykłej utraty siły nabywczej 1 − R/C.

## Bieg 1: 1929–2025 (w próbie Wielki Kryzys, WWII, stagflacja, 2022)

Benchmark dochodowy: PKB nominalny/os. Jednostka testowana:

$$JW(t) = \sqrt{CPI(t) \cdot \text{Dochód}(t)}$$

| Kandydat | % okien zero-regret | Mediana | p95 | Najgorszy przypadek |
|---|---|---|---|---|
| **JW = √(CPI×dochód)** | **97%** | **0,0%** | **1,4%** | **19,7%** (wierzyciel, 1929→1932) |
| CPI | 95% | 0,0% | 2,9% | 43,3% (dłużnik, 1929→1932) |
| dochód | 95% | 0,0% | 2,9% | 43,3% (wierzyciel, 1929→1932) |
| nominal | 2% | 33,0% | 283,1% | **383,6%** (wierzyciel, 1965→1995) |

## Bieg 2: 1939–2025, punkt odniesienia dłużnika to płaca

Punktem odniesienia jest płaca godzinowa pracowników produkcyjnych w przemyśle. Wariant z PKB na osobę w tej tabeli oceniamy względem płac.

| Kandydat | % okien zero-regret | Mediana | p95 | Najgorszy przypadek |
|---|---|---|---|---|
| **JW(CPI, płaca)** | **88%** | **0,0%** | **3,5%** | **6,1%** (dłużnik, 1978→2008) |
| CPI | 79% | 0,0% | 7,1% | 12,5% (dłużnik, 1978→2008) |
| płaca | 79% | 0,0% | 7,1% | 12,5% (wierzyciel, 1978→2008) |
| JW(CPI, PKB/os.) | 49% | 2,2% | 23,7% | 34,0% (dłużnik, 1977→2007) |
| PKB/os. | 20% | 8,8% | 50,7% | 63,2% (dłużnik, 1977→2007) |
| nominal | 1% | 32,5% | 301,7% | 383,6% (wierzyciel, 1965→1995) |

## Interpretacja

- **1929–2025, CPI i PKB na osobę.** Maksimum w badanych oknach to 19,7% (1929–1932). Jest to ocena względem PKB na osobę.
- **1939–2025, CPI i płace.** Maksimum wynosi 6,1% (1978–2008). W 88% okien wynik był poniżej tolerancji. Kontrola zakresu na tych samych danych dla wszystkich całkowitych horyzontów od 3 do 30 lat dała maksimum **7,0551% (1978–1993)**. To dodatkowy wynik, poza pierwotną tabelą.
- **Spłata nominalna 1965–1995.** Żal wierzyciela 383,6% odpowiada odzyskaniu około 21% początkowej siły nabywczej, czyli utracie około 79% według CPI.
- Przy jednakowej wadze obu miar średnia geometryczna daje równe ilorazy R/W i C/R. Etykieta strony przy maksimum Talenta w tabeli pochodzi z wyboru w kodzie przy dwóch równych teoretycznie odchyleniach.

## Ograniczenia

Płace w tej próbie dotyczą jednej grupy pracowników. Wyniki zależą od doboru serii, lat i horyzontów. Test używa rocznych danych historycznych i uproszczonego indeksu. Badanie skutków opóźnień, rewizji oraz dostępności danych w dniu publikacji wymaga innego schematu testu. Obecne prace nad prototypem dotyczą Polski. [Metoda i dowód](../strona/whitepaper.md)
