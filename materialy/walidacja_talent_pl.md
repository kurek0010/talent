# Talent w polskich umowach · wyniki walidacji

**Data:** 2026-11-15. Badanie porównawcze dla rozliczeń w PLN. Wyniki dotyczą określonych reguł, harmonogramów i danych opisanych poniżej.

## Wyniki istotne dla umowy

- **Znaczenie harmonogramu.** Dla jednej płatności maksimum żalu Talenta wyniosło 10,42% przy pięciu dawnych horyzontach, 10,57% przy wszystkich horyzontach 3–30 lat i 17,43% po dodaniu horyzontów 1–2 lata. Dla rat maksimum 17,43% pojawia się już w umowach trzyletnich i dłuższych. W pięcioletniej umowie z 1989 r. decyduje rata w 1991 r., której nie obejmuje pomiar wyłącznie na koniec umowy.
- **Ceny i dochody prowadzą do różnych rezultatów.** W symulacji faktury 2021–2022 nominalna płatność straciła 12,61% siły nabywczej. CPI zachowało tę siłę nabywczą kosztem wzrostu obciążenia względem budżetu kupującego. Przy Talencie obciążenie względem budżetu wzrosło o 1,05%, a realny ubytek sprzedawcy wyniósł 1,04%. W 2014–2015 wszystkie cztery metody dały zerowy żal, choć prowadziły do innych kwot.
- **Niższy żal może iść w parze z większą potrzebą finansowania.** W pożyczce z lat 1989–1994 przy 5% odsetek nominalna kwota tworzy w modelu lukę wierzyciela, indeksacja CPI tworzy wyższą lukę dłużnika niż Talent, a indeksacja płacami przekłada część kosztu na wierzyciela. Przy szokach po obu stronach żaden wariant nie ma najmniejszej luki dla obu jednocześnie. W całej próbie dla rat z 5% Talent daje trochę częstszą modelową lukę dłużnika niż CPI lub płace. Wynik zależy od przyjętego budżetu i rezerwy.
- **Wygenerowanie poprawnego odczytu ma znaczenie odrębne od wzoru.** Przy czterech równych ratach bazowych w 2026 r. suma według opublikowanych kotwic TLN wyniosłaby 10 026,12 zł. Użycie regularnego CPI dostępnego przed odcięciem, przy tej samej nodze płacowej, daje 10 062,42 zł. Różnica 36,30 zł dotyczy tego harmonogramu. Cztery dynamiki CPI w tabeli listopadowej były identyczne z dostępnymi przed właściwymi odcięciami.

## Dane i wspólny harmonogram

Badanie roczne wykorzystuje zapisane w `regret_poland.py` średnie roczne CPI oraz wynagrodzenia w gospodarce narodowej z lat 1989–2024. To ocena retrospektywna na późniejszej migawce danych. Daty startu i płatności są rocznymi punktami odniesienia. Średnia roczna może obejmować dane, które w danej dacie płatności jeszcze nie były znane. Wykorzystano 615 okien dla każdego rodzaju umowy, ze wszystkimi rocznikami startu w horyzontach 1–30 lat mieszczących się w próbie. Krótsze okna pozwalają pokazać roczne faktury oraz wczesne raty. Nominalne poziomy płac zostały zweryfikowane z GUS po denominacji. Przyjęty łącznik 11,1% w 1999 r. jest przybliżeniem. Warianty 5%, 11,1% i 20% służą analizie wrażliwości i nie wyznaczają przedziału ufności. [Seria CPI OECD/FRED](https://fred.stlouisfed.org/series/POLCPIALLMINMEI) · [Tablica płac GUS](https://stat.gov.pl/obszary-tematyczne/rynek-pracy/pracujacy-zatrudnieni-wynagrodzenia-koszty-pracy/przecietne-miesieczne-wynagrodzenie-w-gospodarce-narodowej-w-latach-1950-2025%2C2%2C1.html) · [Audyt wejść i kotwic](audyt_kotwic_2026.md)

Symulowany kontrakt opiewa na **100 000 zł w cenach roku startu**. Kwota ujednolica skalę prób i pozwala odczytać wynik w złotych. Wczesne przykłady są przeliczeniami na wspólną jednostkę PLN po denominacji.

- **Jedna płatność odroczona.** Całość na końcu okna, bez odsetek i opłat. Jednym zastosowaniem jest faktura za maszynę z odroczonym terminem.
- **Pożyczka ratalna.** Jedna rata rocznie, kapitał spłacany w równych częściach w jednostce bazowej. Badamy 0% i 5% odsetek rocznie od pozostałego kapitału w tej jednostce. Opłaty wynoszą zero. Stopy są wspólnymi parametrami scenariusza i nie odzwierciedlają ofert rynkowych.
- **Porównanie reguł.** Każdą kwotę z ustalonego harmonogramu mnożymy odpowiednio przez 1, wskaźnik cen `C`, wskaźnik płac `W` lub `√(CW)`. `C` i `W` oznaczają ilorazy między rokiem płatności a rokiem startu. Dłużnik i wierzyciel rozliczają tę samą kwotę w PLN. Waloryzacja obejmuje całą ratę, łącznie z odsetkami bazowymi.

## Miary i model płynności

| Miara | Definicja |
|---|---|
| Żal dłużnika i wierzyciela | Dla mnożnika waloryzacji `R` obliczamy odpowiednio `max(0, R/W − 1)` i `max(0, C/R − 1)`. Maksimum jednej umowy obejmuje obie strony i wszystkie jej daty płatności. Obciążenie odsetkami mierzymy osobno. |
| Ubytek siły nabywczej ze znakiem | `1 − suma wpływów deflowanych przez C / suma płatności bazowych`. Ujemny ubytek oznacza wyższą siłę nabywczą niż w harmonogramie bazowym. Bez odrębnej stopy dyskontowej i bez wniosków o rentowności wierzyciela. |
| Obciążenie | Najwyższy iloraz płatności i dochodu w danym oknie. Dla faktury mianownikiem jest budżet kupującego na dzień zapłaty. |
| Wzrost rat | Zmiana pierwszej płatności względem jej kwoty bazowej i największa dodatnia zmiana między kolejnymi rzeczywistymi ratami to dwie różne wielkości. Myślnik oznacza brak poprzedniej raty. |
| Luka płynności | Największy niedobór środków względem ścieżki przepływów, po wykorzystaniu zadanej rezerwy i zatrzymanych nadwyżek. Wyrażamy go w złotych o sile nabywczej z roku startu. Odsetek okien z luką opisuje badane kontrakty modelowe. |

Dla rat roczny dochód dłużnika w bazie to 100 000 zł i w scenariuszu bazowym zmienia się z płacami. Na obsługę długu przypada 25% dochodu po przyjęciu pozostałych wydatków jako danych. Przy fakturze budżet kupującego na dzień płatności to 100 000 zł przemnożone przez dynamikę płac. Dla wierzyciela wymagalny wypływ na datę raty lub faktury wynosi 90% kwoty bazowej zwaloryzowanej CPI. To założenie o potrzebach gotówkowych wierzyciela, np. o finansowaniu kosztów już poniesionych. Rezerwa początkowa dla każdej strony wynosi 5 000 zł w cenach startu. Przepływy są deflowane przez CPI i sumowane osobno dla stron. Gdy skumulowana wartość rezerwy i przepływów jest ujemna, jej najgłębszy niedobór wyznacza zapotrzebowanie na dodatkowe finansowanie.

Testujemy dochód lub budżet o 25% niższy od ścieżki bazowej, koszty lub inne wypływy wierzyciela o 20% wyższe od bazowych, oba szoki łącznie oraz większą rezerwę 15 000 zł. Odchylenia obowiązują od pierwszej do ostatniej płatności. Model zakłada utrzymanie harmonogramu, dostępność uzupełniającego finansowania i brak kosztu tego finansowania. Luka identyfikuje wielkość wymaganych środków. Ocena niewypłacalności, rezygnacji z kontraktu i trwałości współpracy wymagałaby danych o bilansie, dostępności kredytu i pozostałych zobowiązaniach.

## Jak czytać porównanie z 2026 r.

Sprawdzamy cztery modelowe raty po 2 500 zł każda z kotwicami za czerwiec–wrzesień i bazą w maju 2026 r. Rozróżniamy rzeczywiście użyte wejście, regularny CPI dostępny przed właściwym odcięciem i późniejszy odczyt z tabeli GUS. W każdej ścieżce stosujemy tę samą, historycznie użytą nogę płacową z przybliżeniem płacy rocznej. Przy wariancie faktycznie opublikowanym korzystamy bezpośrednio z zapisanych kotwic TLN i poziomów jego składników. To izoluje jeden zaobserwowany błąd operacyjny. Daty i wartości przed odcięciem są udokumentowane w komunikatach GUS, a odczyt późniejszy w logu z listopada. [Audyt publikacji](audyt_kotwic_2026.md) · [Listopadowe uruchomienie](https://github.com/kurek0010/talent/actions/runs/43265001848)

Dostępna historia pozwala na to porównanie tylko dla wskazanych miesięcy. Pełna próba roczna nie stanowi symulacji informacji dostępnych na datę historycznej raty. Przepływy z dziennej interpolacji i z nogi płacowej TIP-0003 wymagają osobnej walidacji na archiwum rzeczywistych cykli. Nie ma jeszcze zatwierdzonej serii rozliczeniowej TIP-0003. [TIP-0003](../TIP/TIP-0003-tln-pln-prospektywny.md)

## Niezależne odtworzenie

Z katalogu repozytorium uruchom kod w Pythonie 3.10 lub nowszym. Porównanie z 2026 r. wymaga dostępu do archiwalnego commita kotwic wskazanego w pliku wejściowym. Skrypt korzysta z zapisanych wejść i niczego nie pobiera.

```bash
python3 prototyp/src/walidacja_pl.py
python3 prototyp/src/walidacja_pl.py --csv /tmp/talent-walidacja-okna.csv
python3 -m unittest discover -s prototyp/tests
```

Pierwsza komenda odtwarza tabele poniżej. Druga tworzy 7 500 wierszy obejmujących 7 380 wyników siatki podstawowej i 120 wyników scenariuszy wrażliwości. Wymaga nowej ścieżki wyjściowej. Pola procentowe w CSV mają postać ułamków, a liczby poza CSV pokazujemy po zaokrągleniu. [Kod](../prototyp/src/walidacja_pl.py) · [Dane kontroli z 2026 r.](../prototyp/data/manual/walidacja_cpi_2026.json)

## Wyniki łączne · wszystkie roczniki i horyzonty 1–30 lat

| Umowa | Oprocentowanie | Metoda | Mediana żalu | Maks. żal | Mediana realnego ubytku | Szczyt obciążenia | Maks. wzrost pierwszej płatności | Maks. podwyżka między ratami | Luka dłużnika, odsetek okien | Luka wierzyciela, odsetek okien |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| odroczona | 0,00% | Nominał | 52,82% | 10812,54% (1989–2019) | 34,56% | 97,02% | 0,00% | — | 0,00% | 78,21% |
| odroczona | 0,00% | CPI | 0,00% | 37,90% (1989–1991) | 0,00% | 137,90% | 10812,54% | — | 1,30% | 0,00% |
| odroczona | 0,00% | Płace | 0,00% | 37,90% (1989–1991) | -33,17% | 100,00% | 19092,47% | — | 0,00% | 0,98% |
| odroczona | 0,00% | Talent | 0,00% | 17,43% (1989–1991) | -15,40% | 117,43% | 14372,00% | — | 1,14% | 0,00% |
| raty | 0,00% | Nominał | 52,82% | 10812,54% (1989–2019) | 20,70% | 97,02% | 0,00% | 0,00% | 14,63% | 62,76% |
| raty | 0,00% | CPI | 0,00% | 37,90% (1989–1991) | 0,00% | 134,11% | 567,85% | 76,77% | 16,75% | 0,00% |
| raty | 0,00% | Płace | 0,00% | 37,90% (1989–1991) | -17,10% | 100,00% | 397,99% | 71,91% | 16,59% | 1,95% |
| raty | 0,00% | Talent | 0,00% | 17,43% (1989–1991) | -8,16% | 115,81% | 476,70% | 74,32% | 16,75% | 0,00% |
| raty | 5,00% | Nominał | 52,82% | 10812,54% (1989–2019) | 19,29% | 101,87% | 0,00% | 0,00% | 16,91% | 63,58% |
| raty | 5,00% | CPI | 0,00% | 37,90% (1989–1991) | 0,00% | 140,81% | 567,85% | 73,23% | 21,46% | 0,00% |
| raty | 5,00% | Płace | 0,00% | 37,90% (1989–1991) | -16,13% | 105,00% | 397,99% | 68,47% | 21,79% | 4,88% |
| raty | 5,00% | Talent | 0,00% | 17,43% (1989–1991) | -7,66% | 121,60% | 476,70% | 70,83% | 21,95% | 0,00% |

## Zmiana zakresu próby · Talent

| Zakres | Okna na wariant | Najgorszy żal · jedna płatność | Najgorszy żal · raty |
| --- | --- | --- | --- |
| Pięć horyzontów z dawnego raportu | 112 | 10,42% (1989–1994) | 17,43% (1989–1992) |
| Wszystkie horyzonty 3–30 | 546 | 10,57% (1989–1993) | 17,43% (1989–1992) |
| Wszystkie horyzonty 1–30 | 615 | 17,43% (1989–1991) | 17,43% (1989–1991) |
| Roczniki startu od 1999 | 325 | 1,05% (2021–2022) | 1,05% (2021–2022) |

## Horyzonty · maksymalny żal we wszystkich rocznikach

| Lata | Roczniki startu | Okna | Nominał · odroczona | CPI · odroczona | Płace · odroczona | Talent · odroczona | Nominał · raty | CPI · raty | Płace · raty | Talent · raty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1989–2023 | 35 | 567,85% | 34,11% | 34,11% | 15,81% | 567,85% | 34,11% | 34,11% | 15,81% |
| 2 | 1989–2022 | 34 | 1080,56% | 37,90% | 37,90% | 17,43% | 1080,56% | 37,90% | 37,90% | 17,43% |
| 3 | 1989–2021 | 33 | 1624,79% | 21,50% | 21,50% | 10,23% | 1624,79% | 37,90% | 37,90% | 17,43% |
| 4 | 1989–2020 | 32 | 2262,34% | 22,26% | 22,26% | 10,57% | 2262,34% | 37,90% | 37,90% | 17,43% |
| 5 | 1989–2019 | 31 | 3041,70% | 21,92% | 21,92% | 10,42% | 3041,70% | 37,90% | 37,90% | 17,43% |
| 6 | 1989–2018 | 30 | 3919,85% | 18,29% | 18,29% | 8,76% | 3919,85% | 37,90% | 37,90% | 17,43% |
| 7 | 1989–2017 | 29 | 4715,57% | 14,05% | 14,05% | 6,79% | 4715,57% | 37,90% | 37,90% | 17,43% |
| 8 | 1989–2016 | 28 | 5433,73% | 7,74% | 7,74% | 3,80% | 5433,73% | 37,90% | 37,90% | 17,43% |
| 9 | 1989–2015 | 27 | 6075,52% | 3,01% | 3,01% | 1,50% | 6075,52% | 37,90% | 37,90% | 17,43% |
| 10 | 1989–2014 | 26 | 6517,33% | 0,00% | 0,00% | 0,00% | 6517,33% | 37,90% | 37,90% | 17,43% |
| 11 | 1989–2013 | 25 | 7172,45% | 0,00% | 0,00% | 0,00% | 7172,45% | 37,90% | 37,90% | 17,43% |
| 12 | 1989–2012 | 24 | 7565,77% | 0,00% | 0,00% | 0,00% | 7565,77% | 37,90% | 37,90% | 17,43% |
| 13 | 1989–2011 | 23 | 7711,83% | 0,00% | 0,00% | 0,00% | 7711,83% | 37,90% | 37,90% | 17,43% |
| 14 | 1989–2010 | 22 | 7765,16% | 0,00% | 0,00% | 0,00% | 7765,16% | 37,90% | 37,90% | 17,43% |
| 15 | 1989–2009 | 21 | 8031,21% | 0,00% | 0,00% | 0,00% | 8031,21% | 37,90% | 37,90% | 17,43% |
| 16 | 1989–2008 | 20 | 8208,78% | 0,00% | 0,00% | 0,00% | 8208,78% | 37,90% | 37,90% | 17,43% |
| 17 | 1989–2007 | 19 | 8315,52% | 0,00% | 0,00% | 0,00% | 8315,52% | 37,90% | 37,90% | 17,43% |
| 18 | 1989–2006 | 18 | 8522,44% | 0,00% | 0,00% | 0,00% | 8522,44% | 37,90% | 37,90% | 17,43% |
| 19 | 1989–2005 | 17 | 8881,56% | 0,00% | 0,00% | 0,00% | 8881,56% | 37,90% | 37,90% | 17,43% |
| 20 | 1989–2004 | 16 | 9222,45% | 0,00% | 0,00% | 0,00% | 9222,45% | 37,90% | 37,90% | 17,43% |
| 21 | 1989–2003 | 15 | 9463,03% | 0,00% | 0,00% | 0,00% | 9463,03% | 37,90% | 37,90% | 17,43% |
| 22 | 1989–2002 | 14 | 9868,44% | 0,00% | 0,00% | 0,00% | 9868,44% | 37,90% | 37,90% | 17,43% |
| 23 | 1989–2001 | 13 | 10223,36% | 0,00% | 0,00% | 0,00% | 10223,36% | 37,90% | 37,90% | 17,43% |
| 24 | 1989–2000 | 12 | 10325,77% | 0,00% | 0,00% | 0,00% | 10325,77% | 37,90% | 37,90% | 17,43% |
| 25 | 1989–1999 | 11 | 10331,37% | 0,00% | 0,00% | 0,00% | 10331,37% | 37,90% | 37,90% | 17,43% |
| 26 | 1989–1998 | 10 | 10240,19% | 0,00% | 0,00% | 0,00% | 10331,37% | 37,90% | 37,90% | 17,43% |
| 27 | 1989–1997 | 9 | 10171,45% | 0,00% | 0,00% | 0,00% | 10331,37% | 37,90% | 37,90% | 17,43% |
| 28 | 1989–1996 | 8 | 10384,69% | 0,00% | 0,00% | 0,00% | 10384,69% | 37,90% | 37,90% | 17,43% |
| 29 | 1989–1995 | 7 | 10574,77% | 0,00% | 0,00% | 0,00% | 10574,77% | 37,90% | 37,90% | 17,43% |
| 30 | 1989–1994 | 6 | 10812,54% | 0,00% | 0,00% | 0,00% | 10812,54% | 37,90% | 37,90% | 17,43% |

## Przykłady · faktura z rocznym odroczeniem, bez odsetek

| Okno | Metoda | Płatność (zł) | Żal D | Żal W | Ubytek realny sprzedawcy | Płatność / budżet kupującego | Luka kupującego (zł realne) | Luka sprzedawcy (zł realne) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2014–2015 | Nominał | 100 000,00 | 0,00% | 0,00% | -0,88% | 97,02% | 0,00 | 0,00 |
| 2014–2015 | CPI | 99 125,91 | 0,00% | 0,00% | 0,00% | 96,17% | 0,00 | 0,00 |
| 2014–2015 | Płace | 103 074,43 | 0,00% | 0,00% | -3,98% | 100,00% | 0,00 | 0,00 |
| 2014–2015 | Talent | 101 080,89 | 0,00% | 0,00% | -1,97% | 98,07% | 0,00 | 0,00 |
| 2021–2022 | Nominał | 100 000,00 | 0,00% | 14,43% | 12,61% | 89,23% | 0,00 | 0,00 |
| 2021–2022 | CPI | 114 429,47 | 2,10% | 0,00% | 0,00% | 102,10% | 0,00 | 0,00 |
| 2021–2022 | Płace | 112 072,70 | 0,00% | 2,10% | 2,06% | 100,00% | 0,00 | 0,00 |
| 2021–2022 | Talent | 113 244,95 | 1,05% | 1,05% | 1,04% | 101,05% | 0,00 | 0,00 |

## Przykłady · raty, 5%

| Okno | Metoda | Suma nominalna (zł) | Żal D | Żal W | Ubytek realny wierzyciela | Najwyższa rata / dochód | Wzrost pierwszej raty | Wzrost między ratami | Luka D (zł realne) | Luka W (zł realne) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Transformacja (1989–1994) | Nominał | 115 000,00 | 0,00% | 3041,70% | 92,43% | 5,02% | 0,00% | 0,00% | 0,00 | 89 790,52 |
| Transformacja (1989–1994) | CPI | 2 026 470,69 | 37,90% | 0,00% | 0,00% | 33,53% | 567,85% | 69,70% | 11 700,57 | 0,00 |
| Transformacja (1989–1994) | Płace | 1 622 688,96 | 0,00% | 37,90% | 21,57% | 25,00% | 397,99% | 65,03% | 0,00 | 8 306,45 |
| Transformacja (1989–1994) | Talent | 1 812 883,97 | 17,43% | 17,43% | 11,47% | 28,95% | 476,70% | 67,35% | 545,31 | 0,00 |
| Spadek inflacji (1999–2004) | Nominał | 115 000,00 | 0,00% | 22,88% | 14,31% | 22,18% | 0,00% | 0,00% | 0,00 | 0,00 |
| Spadek inflacji (1999–2004) | CPI | 134 382,13 | 0,00% | 0,00% | 0,00% | 24,37% | 9,90% | 1,19% | 0,00 | 0,00 |
| Spadek inflacji (1999–2004) | Płace | 142 468,56 | 0,00% | 0,00% | -5,93% | 25,00% | 12,72% | 2,89% | 0,00 | 0,00 |
| Spadek inflacji (1999–2004) | Talent | 138 356,74 | 0,00% | 0,00% | -2,92% | 24,69% | 11,30% | 2,04% | 0,00 | 0,00 |
| Okno porównawcze (2009–2014) | Nominał | 115 000,00 | 0,00% | 11,90% | 7,80% | 24,05% | 0,00% | 0,00% | 0,00 | 0,00 |
| Okno porównawcze (2009–2014) | CPI | 124 879,36 | 0,00% | 0,00% | 0,00% | 24,67% | 2,58% | 0,07% | 0,00 | 0,00 |
| Okno porównawcze (2009–2014) | Płace | 129 864,83 | 0,00% | 0,00% | -3,93% | 25,00% | 3,93% | 1,20% | 0,00 | 0,00 |
| Okno porównawcze (2009–2014) | Talent | 127 337,00 | 0,00% | 0,00% | -1,94% | 24,84% | 3,25% | 0,63% | 0,00 | 0,00 |
| Deflacja, potem wzrost cen (2014–2019) | Nominał | 115 000,00 | 0,00% | 4,61% | 0,83% | 24,25% | 0,00% | 0,00% | 0,00 | 0,00 |
| Deflacja, potem wzrost cen (2014–2019) | CPI | 116 013,09 | 0,00% | 0,00% | 0,00% | 24,04% | -0,87% | 0,00% | 0,00 | 0,00 |
| Deflacja, potem wzrost cen (2014–2019) | Płace | 131 367,72 | 0,00% | 0,00% | -13,09% | 25,00% | 3,07% | 2,67% | 0,00 | 0,00 |
| Deflacja, potem wzrost cen (2014–2019) | Talent | 123 390,90 | 0,00% | 0,00% | -6,29% | 24,52% | 1,08% | 0,00% | 0,00 | 0,00 |
| Pandemia i inflacja (2019–2024) | Nominał | 115 000,00 | 0,00% | 43,84% | 17,16% | 23,79% | 0,00% | 0,00% | 0,00 | 3 236,02 |
| Pandemia i inflacja (2019–2024) | CPI | 141 188,21 | 0,00% | 0,00% | 0,00% | 24,60% | 3,37% | 9,66% | 0,00 | 0,00 |
| Pandemia i inflacja (2019–2024) | Płace | 150 520,54 | 0,00% | 0,00% | -6,19% | 25,00% | 5,07% | 9,14% | 0,00 | 0,00 |
| Pandemia i inflacja (2019–2024) | Talent | 145 741,80 | 0,00% | 0,00% | -3,02% | 24,80% | 4,22% | 8,53% | 0,00 | 0,00 |

## Wrażliwość · luka dłużnika / wierzyciela w realnych PLN

| Okno | Umowa | Scenariusz | Nominał | CPI | Płace | Talent |
| --- | --- | --- | --- | --- | --- | --- |
| 1989–1994 | raty | bazowy | 0,00 / 89 790,52 | 11 700,57 / 0,00 | 0,00 / 8 306,45 | 545,31 / 0,00 |
| 1989–1994 | raty | dochód −25% | 0,00 / 89 790,52 | 36 275,43 / 0,00 | 11 468,98 / 8 306,45 | 23 081,90 / 0,00 |
| 1989–1994 | raty | koszty +20% | 0,00 / 110 490,52 | 11 700,57 / 4 200,00 | 0,00 / 29 006,45 | 545,31 / 17 393,53 |
| 1989–1994 | raty | oba szoki, rezerwa 5% | 0,00 / 110 490,52 | 36 275,43 / 4 200,00 | 11 468,98 / 29 006,45 | 23 081,90 / 17 393,53 |
| 1989–1994 | raty | oba szoki, rezerwa 15% | 0,00 / 100 490,52 | 26 275,43 / 0,00 | 1 468,98 / 19 006,45 | 13 081,90 / 7 393,53 |
| 1989–1994 | odroczona | bazowy | 0,00 / 81 817,01 | 12 976,76 / 0,00 | 0,00 / 2 976,76 | 3 543,44 / 0,00 |
| 1989–1994 | odroczona | dochód −25% | 0,00 / 81 817,01 | 33 482,57 / 0,00 | 15 505,81 / 2 976,76 | 24 049,25 / 0,00 |
| 1989–1994 | odroczona | koszty +20% | 0,00 / 99 817,01 | 12 976,76 / 3 000,00 | 0,00 / 20 976,76 | 3 543,44 / 12 433,32 |
| 1989–1994 | odroczona | oba szoki, rezerwa 5% | 0,00 / 99 817,01 | 33 482,57 / 3 000,00 | 15 505,81 / 20 976,76 | 24 049,25 / 12 433,32 |
| 1989–1994 | odroczona | oba szoki, rezerwa 15% | 0,00 / 89 817,01 | 23 482,57 / 0,00 | 5 505,81 / 10 976,76 | 14 049,25 / 2 433,32 |
| 2009–2014 | raty | bazowy | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 |
| 2009–2014 | raty | dochód −25% | 5 161,04 / 0,00 | 12 421,82 / 0,00 | 16 937,45 / 0,00 | 14 648,13 / 0,00 |
| 2009–2014 | raty | koszty +20% | 0,00 / 13 174,84 | 0,00 / 4 200,00 | 0,00 / 0,00 | 0,00 / 1 973,70 |
| 2009–2014 | raty | oba szoki, rezerwa 5% | 5 161,04 / 13 174,84 | 12 421,82 / 4 200,00 | 16 937,45 / 0,00 | 14 648,13 / 1 973,70 |
| 2009–2014 | raty | oba szoki, rezerwa 15% | 0,00 / 3 174,84 | 2 421,82 / 0,00 | 6 937,45 / 0,00 | 4 648,13 / 0,00 |
| 2009–2014 | odroczona | bazowy | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 |
| 2009–2014 | odroczona | dochód −25% | 2 642,86 / 0,00 | 13 273,52 / 0,00 | 22 242,16 / 0,00 | 17 661,57 / 0,00 |
| 2009–2014 | odroczona | koszty +20% | 0,00 / 13 630,66 | 0,00 / 3 000,00 | 0,00 / 0,00 | 0,00 / 0,00 |
| 2009–2014 | odroczona | oba szoki, rezerwa 5% | 2 642,86 / 13 630,66 | 13 273,52 / 3 000,00 | 22 242,16 / 0,00 | 17 661,57 / 0,00 |
| 2009–2014 | odroczona | oba szoki, rezerwa 15% | 0,00 / 3 630,66 | 3 273,52 / 0,00 | 12 242,16 / 0,00 | 7 661,57 / 0,00 |
| 2019–2024 | raty | bazowy | 0,00 / 3 236,02 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 |
| 2019–2024 | raty | dochód −25% | 2 347,76 / 3 236,02 | 10 913,03 / 0,00 | 17 345,11 / 0,00 | 13 704,78 / 0,00 |
| 2019–2024 | raty | koszty +20% | 0,00 / 23 936,02 | 0,00 / 4 200,00 | 0,00 / 0,00 | 0,00 / 723,45 |
| 2019–2024 | raty | oba szoki, rezerwa 5% | 2 347,76 / 23 936,02 | 10 913,03 / 4 200,00 | 17 345,11 / 0,00 | 13 704,78 / 723,45 |
| 2019–2024 | raty | oba szoki, rezerwa 15% | 0,00 / 13 936,02 | 913,03 / 0,00 | 7 345,11 / 0,00 | 3 704,78 / 0,00 |
| 2019–2024 | odroczona | bazowy | 0,00 / 15 479,49 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 |
| 2019–2024 | odroczona | dochód −25% | 0,00 / 15 479,49 | 8 260,82 / 0,00 | 23 913,06 / 0,00 | 15 802,55 / 0,00 |
| 2019–2024 | odroczona | koszty +20% | 0,00 / 33 479,49 | 0,00 / 3 000,00 | 0,00 / 0,00 | 0,00 / 0,00 |
| 2019–2024 | odroczona | oba szoki, rezerwa 5% | 0,00 / 33 479,49 | 8 260,82 / 3 000,00 | 23 913,06 / 0,00 | 15 802,55 / 0,00 |
| 2019–2024 | odroczona | oba szoki, rezerwa 15% | 0,00 / 23 479,49 | 0,00 / 0,00 | 13 913,06 / 0,00 | 5 802,55 / 0,00 |

## Warianty łączenia serii w 1999 r.

| Łącznik | Maks. żal kwoty odroczonej | Maks. żal rat | Mediana ubytku wierzyciela dla płatności odroczonej |
| --- | --- | --- | --- |
| 5,00% | 2,53% | 17,43% | -21,57% |
| 11,10% | 0,00% | 17,43% | -25,05% |
| 20,00% | 0,00% | 17,43% | -29,96% |

## Publikacje 2026 · odczyt przed odcięciem, odczyt użyty i późniejsza tabela

| Miesiąc | Regularny komunikat GUS | Dzień odcięcia | CPI użyty | CPI przed odcięciem | CPI w listopadzie | Rata TLN z publikacji (zł) | Rata TLN z CPI dostępnego przed odcięciem (zł) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06 | [2026-07-15](https://stat.gov.pl/obszary-tematyczne/ceny-handel/wskazniki-cen/wskazniki-cen-towarow-i-uslug-konsumpcyjnych-w-czerwcu-2026-r-%2C2%2C176.html) | 2026-07-24 | 99,70 | 99,50 | 99,50 | 2 502,12 | 2 499,61 |
| 2026-07 | [2026-08-13](https://stat.gov.pl/kalendarium/13-08-2026.html) | 2026-08-24 | 100,00 | 100,80 | 100,80 | 2 508,00 | 2 515,49 |
| 2026-08 | [2026-09-15](https://publikacje.new.stat.gov.pl/portal-publikacje/wskazniki-cen-towarow-i-uslug-konsumpcyjnych-w-sierpniu-2026-r) | 2026-09-24 | 100,00 | 100,30 | 100,30 | 2 508,00 | 2 519,26 |
| 2026-09 | [2026-10-14](https://stat.gov.pl/obszary-tematyczne/ceny-handel/wskazniki-cen/wskazniki-cen-towarow-i-uslug-konsumpcyjnych-we-wrzesniu-2026-r-%2C2%2C179.html) | 2026-10-24 | 100,00 | 100,70 | 100,70 | 2 508,00 | 2 528,06 |

| Wejścia | Nominał | CPI | Płace | Talent |
| --- | --- | --- | --- | --- |
| opublikowane | 10 000,00 | 9 969,99 | 10 082,58 | 10 026,12 |
| odczyty znane przed odcięciem | 10 000,00 | 10 042,35 | 10 082,58 | 10 062,42 |
| tabela listopadowa | 10 000,00 | 10 042,35 | 10 082,58 | 10 062,42 |
