# Talent umowy międzynarodowej — wyniki PL-US (2002–2024)

**Data:** 2026-07-04 · **Kod:** `prototyp/src/regret_bilateral.py`

**Korekta 2026-11-15.** Zawężono zakres wniosku do porównanych wariantów i poprawiono długość okna z maksimum. Tabela zachowuje opublikowane liczby.

**Status:** eksperyment PL–US do dalszego zbadania. Obecnie rozwijany TLN-PLN opiera się na danych Polski i rozliczeniach w PLN.

## Konstrukcja

Talent dwustronny (TLN-2) dla umowy polsko-amerykańskiej: **środek geometryczny obu Talentów krajowych z kursem rozłożonym po połowie**:

$$V_{PLN}(t) = \sqrt{TLN_{PL}(t) \cdot TLN_{US}(t) \cdot \frac{S(t)}{S(0)}} \qquad V_{USD}(t) = \frac{V_{PLN}(t)}{S(t)/S(0)}$$

gdzie S to kurs PLN/USD; po stronie USD wzór jest symetryczny.

Żal liczony w obu krajach naraz: jednostka oceniana w PLN względem korytarza [CPI-PL, płaca-PL] i w USD względem [CPI-US, płaca-US]; żal okna = największe przekroczenie któregokolwiek z 4 brzegów (każda strona może być dłużnikiem lub wierzycielem). Wszystkie dostępne lata startu dla horyzontów 3, 5, 10 i 20 lat. „Zero-żal” oznacza wynik poniżej 0,02 w logarytmach, czyli poniżej około 2,02% w skali raportu.

## Wyniki

| Jednostka umowy | % okien zero-żalu | Mediana | p95 | Najgorszy przypadek |
|---|---|---|---|---|
| **TLN-2 dwustronny** | 20% | 5,7% | **23,0%** | **34,3%** (dłużnik US, 2003→2008) |
| TLN-US | 43% | 3,4% | 33,6% | 60,7% (wierzyciel PL, 2003→2008) |
| TLN-PL | 13% | 13,4% | 48,9% | 77,2% (dłużnik US, 2003→2008) |
| USD nominal | 0% | 19,1% | 77,0% | 84,6% |
| 50/50 PLN+USD nominal | 0% | 23,4% | 70,1% | 85,0% |
| PLN nominal | 0% | 30,6% | 77,9% | **93,0%** |

Kontekst próby: płace PL ×3,84 vs płace US ×1,82 (konwergencja), CPI PL ×2,01 vs US ×1,74, kurs bez zmian (×0,98) — realny rozjazd gospodarek ~2×.

## Interpretacja

W tej próbie TLN-2 ma najniższe maksimum spośród wymienionych wariantów, 34,3%, w oknie 2003–2008 (pięć lat). Porównanie wariantów nie ustanawia własności minimaksowej względem czterech ograniczeń. Kontrola dla tego pojedynczego okna dała minimum ex post około 27,95%, wobec około 34,34% dla TLN-2. Minimum jednego okna nie rozstrzyga, jak zaprojektować jedną regułę dla wszystkich okien.

Porównanie innych par gospodarek oraz wersje wielostronne pozostają tematami dalszych badań.

## Zastrzeżenia

Dane roczne; płace PL z tablic GUS/ZUS (do weryfikacji, jak w `materialy/wyniki_kruche_gospodarki.md`); płace US = produkcyjni w przemyśle; kurs = średnia roczna NBP. Wyniki wrażliwe na dobór próby 2002–2024 (jedna wielka konwergencja) — wskazany test na dłuższej parze (np. US-UK od 1939).
