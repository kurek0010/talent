# Polityka danych TLN-PLN — v0.1

**Stan dokumentacji:** 2026-11-15. Opis polskiego prototypu i założeń do rozstrzygnięcia przed wdrożeniem reguły rozliczeniowej. [Reguła publikacyjna](strona/regula_publikacyjna.md)

## 1. Rejestr serii

| Seria | Źródło | Rola |
|---|---|---|
| CPI m/m | GUS, „Miesięczne wskaźniki cen towarów i usług konsumpcyjnych od 1982 roku” | wejście aktualizatora z `first_prints_pln.json` |
| Roczne przeciętne wynagrodzenie w gospodarce narodowej | wartości zapisane w `first_prints_pln.json`, w tym przybliżenie oznaczone jako proxy | wejście aktualizatora, interpolacja logarytmiczna między punktami lipcowymi |
| HICP Polski | Eurostat, geo=PL | kandydat do porównań, wspólna baza źródłowa z CPI |
| Przeciętne wynagrodzenie i zatrudnienie w sektorze przedsiębiorstw | miesięczny komunikat GUS | kandydat na fundusz płac i mianownik MA12 w [TIP-0001](TIP/TIP-0001-noga-placowa-v02.md) |
| Mediana wynagrodzeń w gospodarce narodowej | GUS, „Rozkład wynagrodzeń w gospodarce narodowej” | kandydat w [TIP-0002](TIP/TIP-0002-mediana-wynagrodzen.md) |
| Indeks cen online | źródło do wyboru | dalsza propozycja porównawcza |
| Kursy średnie walut | NBP, tabela A | poglądowe przeliczenia polskiej kotwicy |

Polski CPI i HICP mają wspólne dane i początkowe etapy obliczeń. Rozbieżność dwóch miar może sygnalizować problem, ale sama nie identyfikuje błędnego źródła. [Metadane HICP dla Polski, §18.5.2](https://ec.europa.eu/eurostat/cache/metadata/EN/prc_hicp_esmshi4_pl.htm)

Miesięczny szereg mediany z nowego badania GUS zaczyna się w styczniu 2024 r. Dane za marzec 2026 r. opublikowano 2 września 2026 r. Analiza ewentualnego użycia powinna uwzględniać faktyczne daty publikacji. Dynamika mediany poziomów wynagrodzeń jest inną miarą niż mediana zmian płac tych samych osób. [Zapowiedź GUS](https://stat.gov.pl/dla-mediow/informacje-prasowe/informacja-o-badaniu-rozklad-wynagrodzen-w-gospodarce-narodowej%2C2%2C1.html?contrast=default) · [Kalendarium GUS](https://stat.gov.pl/kalendarium/02-09-2026.html)

Serie z `prototyp/data/raw/` służą badaniom historycznym. Metryki obliczone na tych migawkach nie ustalają wyniku, który byłby dostępny w konkretnym dniu w przeszłości.

## 2. Cykl miesięczny

Workflow zaplanowano na 25. dzień miesiąca. Kod aktualizacji oczekuje wtedy kotwicy za poprzedni miesiąc. Wcześniejszy projekt przewidywał odcięcie 24. dnia o 12:00. Pobranie aktualnej tabeli 25. dnia nie wystarcza do potwierdzenia, że dane były dostępne przed odcięciem.

## 3. Dane używane w obliczeniu

CPI jest łańcuchowany od ostatniego zapisanego poziomu, na podstawie miesięcznej dynamiki zapisanej w rejestrze. Noga płac wykorzystuje roczne punkty przypisane do lipca. Poza zakresem interpolacji aktualizator przenosi ostatni poziom składnika płacowego. Wariant TIP-0001 i mediana nie są w tej ścieżce używane.

## 4. Braki danych

1. Jeden brak dynamiki CPI dla oczekiwanego miesiąca pozwala użyć ostatniej znanej dynamiki. Aktualizator wypisuje alert.
2. Drugi kolejny brak przerywa uruchomienie przed dopisaniem nowych kotwic. Zastąpienie źródła lub przejście na koszyk walut wymaga osobnej decyzji metodologicznej.

## 5. Rewizje pierwszych odczytów

Zasadą projektu jest zachowanie opublikowanych wartości. Łańcuch pierwszych odczytów może odbiegać od łańcucha na danych zrewidowanych. Jeśli pierwsza dynamika wynika z przejścia 100 → 110, urząd rewiduje drugi poziom do 105, a kolejna dynamika wynosi +10% (105 → 115,5), łańcuch pierwszych dynamik daje 121. Poziom zrewidowany wynosi 115,5. Porównanie tych ścieżek w okresowym raporcie pozostaje propozycją.

## 6. Zmiany źródeł i integralność publikacji

Zmiany definicji serii, źródeł i reguł obsługi rewizji wymagają [TIP](TIP/README.md), testu nakładania serii oraz udokumentowanej daty wejścia. Rejestr publikacji przechowuje listę miesięcy. Archiwum z wartościami, datami publikacji wejść, skrótami plików i wersją kodu dla każdej kotwicy wymaga wdrożenia. Raportowanie i odtwarzanie należy prowadzić na odrębnych kopiach danych.

## 7. Odrębna seria próbna

[TIP-0003](TIP/TIP-0003-tln-pln-prospektywny.md) testuje CPI z pierwszej regularnej publikacji i 12-miesięczną średnią z płac w sektorze przedsiębiorstw. Granicą dostępności jest 24. dzień o 12:00 w czasie polskim. Braki wstrzymują cykl. Próbne odczyty, ich wejścia i skróty trafiają do oddzielnego archiwum. Publikacje dotychczasowej serii opisuje [audyt kotwic z 2026 r.](materialy/audyt_kotwic_2026.md).
