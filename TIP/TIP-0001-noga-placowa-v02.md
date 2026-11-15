# TIP-0001: Noga płacowa v0.2 — fundusz płac / wygładzone zatrudnienie

**Autor:** Mariusz Kurowski · **Data:** 2026-07-05 · **Status:** Testowany na danych USA. Aktualizator miesięczny TLN-PLN używa interpolowanych płac rocznych.
**Korekta 2026-11-15.** Status dopasowano do kodu aktualizatora. Część testową zachowano jako wynik historyczny.

## Problem

Zmiana składu zatrudnionych może wpłynąć na przeciętną płacę. Na przykład odpływ osób mniej zarabiających może podnieść średnią w pozostałej grupie nawet przy spadku funduszu płac.

## Proponowana zmiana

```
W(m) = FunduszPłac(m) / MA12(Zatrudnienie)(m)     (średnia krocząca, przyczynowa)
```

Wygładzenie mianownika może zmniejszyć reakcję na krótkotrwałe wahania zatrudnienia. Wariant wykorzystuje fundusz płac i zatrudnienie. Dawna reguła opisywała również dalsze wygładzenie całego indeksu przez MA12. Wyniki poniżej dotyczą wariantu z tabeli.

## Test na danych (przed zmianą reguły)

Dane: USA, miesięczne 2000-01–2026-06 (FRED: AHETPI, PAYEMS; `data/raw/fred_*_monthly_2000_2026.csv`). Wyniki (`data/processed/wage_leg_v2_monthly.csv`):

| Epizod | Przeciętna (stara) | Fundusz/MA12 (nowa) |
|---|---|---|
| IV 2020 (szok COVID), m/m | **+4,2%** | **−8,9%** |
| Wielka recesja IX 2008→XII 2009 | +3,5% | +3,2% |
| Dryf 2000→2026 (26,5 roku) | +135,7% | +136,2% |

## Interpretacja i stan decyzji

W próbie USA różnica między zmianami skumulowanymi wyniosła 0,5 p.p. Efekt miesięczny w kwietniu 2020 r. nie wyznacza zachowania tej miary w innych kryzysach ani w Polsce.

Wariant opisano w dokumentacji 2026-07-05. Przed ewentualnym wdrożeniem w TLN-PLN potrzebne są polskie dane, test dostępności w dniu publikacji i decyzja z datą wejścia w życie.
