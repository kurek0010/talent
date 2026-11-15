# Archiwum — porównanie kandydatów na jednostkę rozliczeniową

**Data raportu:** 2026-07-04 · **Korekta 2026-11-15.** Oznaczono archiwalny status testu i doprecyzowano punkty odniesienia. Tabela zachowuje opublikowane wyniki.

## Zakres i odtwarzalność

Raport obejmował lata 1996–2025 i horyzonty od 3 do 20 lat. Porównywano indeksy dla pojedynczej płatności. Punkty odniesienia stanowiły CPI USA i dochód na osobę na świecie. AUV (Absolute Unit of Value) był wcześniejszą koncepcją opartą m.in. na danych o surowcach. W repozytorium zachowano `prototyp/data/processed/regret_race.csv`. Brakuje pełnych wejść AUV i skryptu reprodukcji. Roczne notowania złota, w tym szacunek za 2025 r., wymagają weryfikacji u źródła.

Pierwotny raport określa kolumnę „zero-żal” jako odchylenie poniżej 2%. Brak skryptu uniemożliwia potwierdzenie skali tego progu.

## Wyniki archiwalne

| Kandydat | % okien zero-żalu | Mediana żalu | p95 | Najgorszy przypadek |
|---|---|---|---|---|
| **MIX A: 50% dochód + 50% CPI (geom.)** | **82%** | **0,0%** | **4,5%** | **7,2%** |
| MIX D: 45/45/10 (dochód/CPI/AUV-kon) | 69% | 0,0% | 7,5% | 9,7% |
| CPI USA | 75% | 0,0% | 9,3% | 14,9% |
| dochód/os. (świat) | 75% | 0,0% | 9,3% | 14,9% |
| dochód wygładzony 3l | 43% | 3,1% | 11,6% | 14,9% |
| MIX B: 60% dochód + 40% AUV-kontrakt | 57% | 1,3% | 23,1% | 25,9% |
| MIX C: 1/3 CPI + 1/3 dochód + 1/3 złoto | 12% | 11,8% | 28,4% | 44,3% |
| **nominal (dzisiejsza praktyka KKOP)** | 0% | 17,7% | 54,0% | 66,1% |
| AUV kontraktowy (wygładzony 5l) | 19% | 15,1% | 58,2% | 68,8% |
| koszyk surowcowy (nominalny) | 13% | 20,0% | 64,8% | 87,6% |
| AUV surowy | 18% | 20,0% | 78,8% | 93,9% |
| złoto | 2% | 47,7% | 189,0% | **264,9%** |

## Interpretacja

Wariant mieszany oparty na CPI i dochodzie miał najniższy raportowany maksymalny żal w zestawieniu. Wybór punktów odniesienia wpływa na kolejność kandydatów. Ocena polskiego TLN-PLN wymaga polskich danych i porównywalnych scenariuszy. [Wynik próby dla Polski](wyniki_kruche_gospodarki.md)
