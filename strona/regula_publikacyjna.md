# Reguła publikacyjna TLN-PLN

Stan prototypu na 2026-11-15. Polski Talent opiera się na krajowych cenach i przeciętnych wynagrodzeniach. Kotwice to miesięczne odczyty badawcze, z bazą 100 w styczniu 1996 r.

## 1. Kotwice miesięczne w obecnym prototypie

Kotwica to średnia geometryczna dodatnich indeksów cen i płac, znormalizowanych do wspólnej bazy.

$$A(m) = 100 \cdot \sqrt{\frac{I_c(m)}{I_c(m_0)} \cdot \frac{I_w(m)}{I_w(m_0)}}$$

- **Ceny.** Aktualizator dokłada dynamikę CPI GUS z rejestru `first_prints_pln.json` do ostatniego indeksu cen. Jeden brakujący miesiąc może zostać uzupełniony przez przeniesienie poprzedniej dynamiki. Przy drugim kolejnym braku aktualizator przerywa uruchomienie bez dopisania nowych kotwic.
- **Płace.** Punkty rocznych przeciętnych wynagrodzeń przypisane do lipca są interpolowane logarytmicznie. Po końcu interpolacji kod przenosi ostatnią wartość indeksu płac. Roczna wartość może być oznaczona jako przybliżenie. Fundusz płac podzielony przez średnią kroczącą zatrudnienia (TIP-0001) był badany osobno i pozostaje poza aktywną ścieżką.
- **Kalendarz.** Od 25. dnia miesiąca aktualizator oczekuje kotwicy za poprzedni miesiąc. Workflow pobiera aktualnie dostępną tabelę GUS. Planowane odcięcie danych 24. dnia o 12:00 wymaga udokumentowania dat faktycznej dostępności wejść.

## 2. Demonstracja wartości dziennych

Skrypt demonstracyjny oblicza osobne kotwice na potrzeby rekonstrukcji i przedłuża wzrost ostatniej kotwicy według wzoru

$$T(d_k) = A(m) \cdot g^{k/K}, \qquad g = \frac{A(m)}{A(m-1)}, \qquad k=1,\ldots,K.$$

Kod stosuje miesiąc kalendarzowy m+1, podczas gdy wcześniejszy projekt przewidywał okno od 26. dnia m+1 do 25. dnia m+2. Jest to ekstrapolacja. Dla kotwic 100, 110, 110 pierwszy odcinek kończy się na 121, a następny zaczyna na 110, co daje spadek o 9,09%. Ścieżka dzienna wymaga osobnej decyzji o wzorze, kalendarzu i ciągłości. Miesięczny workflow jej nie aktualizuje. Skrypt demonstracyjny zapisuje wyniki w osobnym katalogu badawczym.

## 3. Historia publikacji

Projekt przyjmuje zasadę zachowania opublikowanych wartości. Rejestr `talent_published.json` przechowuje miesiące wykorzystane przez aktualizator przy dopisywaniu kotwic. Odtworzono cztery kotwice z miesięcy czerwiec–wrzesień 2026 r. oraz przyczynę użycia zastępczych dynamik CPI. Powiązanie odczytów z dokładną migawką wejść, ich datami i skrótem kodu jest testowane w odrębnej serii prospektywnej według TIP-0003. [Rejestr TIP](../TIP/README.md)

Łańcuch pierwszych odczytów może trwale odbiegać od indeksu obliczonego na danych zrewidowanych. Odtworzenie wyniku wymaga zachowania użytych wersji danych.

## 4. Propozycje do dalszej oceny

W obecnym kodzie przekroczenie 15% bezwzględnej zmiany kotwicy w miesiącu ustawia flagę. Publikacja dekadowa, przełączenie na koszyk walut przy hiperinflacji i alarm rozbieżności źródeł są propozycjami. Częstsze ogłaszanie wartości mogłoby pomóc tylko przy odpowiednio aktualnych wejściach. Polski CPI i HICP częściowo opierają się na wspólnych danych, a rozbieżność dwóch wskaźników nie wskazuje, który zawiera błąd. [Metadane HICP dla Polski, §18.5.2](https://ec.europa.eu/eurostat/cache/metadata/EN/prc_hicp_esmshi4_pl.htm)

Zmiany metody i źródeł przechodzą przez [procedurę TIP](../TIP/README.md). [Specyfikacja obliczeń](../specyfikacja.html) · [Polityka danych](https://github.com/kurek0010/talent/blob/main/POLITYKA_danych_v0.1.md)
