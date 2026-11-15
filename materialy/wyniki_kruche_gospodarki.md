# Talent w kruchych gospodarkach — test Polski i epizody zagraniczne

**Data raportu:** 2026-07-04 · **Korekta 2026-11-15.** Doprecyzowano zakres testu i miarę strat. Usunięto wniosek o 70% straty dla wierzyciela w Argentynie, którego nie uzasadniało porównanie dwóch ścieżek CPI. Tabela wyników Polski zachowuje opublikowane liczby.

## Polska 1989–2024 — wynik warunkowy

Kod: `prototyp/src/regret_poland.py`. CPI pochodzi z FRED/OECD (POLCPIALLMINMEI), a roczne płace pochodzą z tablic wpisanych do skryptu. Weryfikacja 2026-11-15 potwierdziła zgodność 36 poziomów z tablicą GUS po uwzględnieniu denominacji. Przy przejściu z szeregu netto na brutto w 1999 r. skrypt stosuje przybliżoną dynamikę 11,1%. Ta dynamika wciąż wymaga niezależnego potwierdzenia.

Test obejmuje wszystkie dostępne lata startu dla horyzontów 3, 5, 10, 20 i 30 lat. „Zero-żal” oznacza wynik poniżej 0,02 w skali logarytmicznej (około 2,02% w skali tabeli). Test dotyczy jednej płatności i uproszczonego indeksu, bez odwzorowania operacyjnych opóźnień czy braków danych.

| Kandydat | % okien zero-żalu | Mediana | p95 | Najgorszy przypadek |
|---|---|---|---|---|
| **Talent** | **98%** | **0,0%** | **0,0%** | **10,4%** (wierzyciel, 1989→1994) |
| CPI | 98% | 0,0% | 0,0% | 21,9% (dłużnik, 1989→1994) |
| płaca | 98% | 0,0% | 0,0% | 21,9% (wierzyciel, 1989→1994) |
| nominal | 4% | 32,6% | 1 589% | **10 813%** (wierzyciel, 1989→2019) |

Maksimum Talenta wyniosło 10,4% w latach 1989–1994, warunkowo na użytym szeregu płac. Przy symetrii ilorazów obie strony mają w modelu ten sam żal. Etykieta strony w tabeli odzwierciedla wybór w kodzie przy równych teoretycznie odchyleniach. Wartość 10 813% dla spłaty nominalnej oznacza żal C/R − 1, któremu odpowiada odzyskanie poniżej 1% początkowej siły nabywczej.

## Niemcy i Argentyna — materiał porównawczy

Liczby z opisu tych epizodów są przybliżeniami do weryfikacji. Służą do budowania hipotez o ograniczeniach metody.

- **Niemcy 1923.** Przy wzroście cen o 20% w jeden dzień jednodniowe opóźnienie pełnej waloryzacji oznaczałoby spadek siły nabywczej o około 16,7%. To ilustracja kosztu opóźnienia.
- **Argentyna 2002.** Dla wzrostu cen o 41% i płac o 7% model daje wzrost obciążenia względem płac o ok. 14,8% i ubytek siły nabywczej o ok. 12,9%.
- **Argentyna 2007–2015.** Przy identycznej ścieżce płac porównanie mnożników CPI ×2,2 i ×7 daje indeks niższy o około 44% względem wariantu z wyższym CPI. Do oszacowania zmiany siły nabywczej konkretnej spłaty potrzebne są również płace i odpowiedni wskaźnik cen.
- **Kredyty UVA.** Porównanie indeksacji cenowej i mieszanej w epizodzie wzrostu cen i płac może zilustrować zmianę obciążenia ratą. Wpływ na niewypłacalność i działania państwa wymaga osobnych danych i modelu.

## Dalsze prace

Do zbadania pozostają strategia przy opóźnieniu publikacji, zasady kwalifikowania alternatywnych źródeł i umowne postępowanie w kryzysie. Planowane bezpieczniki opisuje [reguła publikacyjna](../strona/regula_publikacyjna.md).
