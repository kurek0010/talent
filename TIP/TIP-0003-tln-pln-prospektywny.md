# TIP-0003 — prospektywne odczyty TLN-PLN

**Data:** 2026-11-15. **Status:** Testowany lokalnie. Kandydat ma oddzielną serię i archiwum. Uruchomienie rozliczeniowe i jego data wymagają decyzji po pilotażu.

## Problem

Dotychczasowa seria zachowuje wartości opublikowane, w tym odczyty z niepełnymi wejściami. Dzienna demonstracja przedłuża dynamikę poprzedniego okresu i może powodować skoki między oknami. [Audyt wybranych publikacji](../materialy/audyt_kotwic_2026.md)

## Definicja testowana

- **Ceny.** Ogólnopolski CPI m/m (poprzedni miesiąc = 100) z pierwszej regularnej informacji sygnalnej GUS za dany miesiąc. Szybki szacunek poprzedzający regularną publikację ma osobny status. Każdy nowy mnożnik CPI wchodzi do łańcucha raz. [Tablica CPI GUS](https://publikacje.new.stat.gov.pl/portal-publikacje/miesieczne-wskazniki-cen-towarow-i-uslug-konsumpcyjnych-od-1982-r)
- **Płace.** Średnia arytmetyczna 12 obserwacji brutto dla sektora przedsiębiorstw, do miesiąca kotwicy włącznie. Baza może korzystać z przekroju dostępnego przed odcięciem. Kolejne obserwacje bierzemy z pierwszej regularnej publikacji. Wybór pozwala uniknąć prognozy płacy całorocznej i ogranicza sezonowość, kosztem wolniejszej reakcji na zmiany płac. Miara obejmuje sektor przedsiębiorstw, reaguje na zmianę składu i służy jako przybliżenie zmian przeciętnych wynagrodzeń. Warianty TIP-0001 i TIP-0002 pozostają propozycjami badawczymi. [Przykładowa informacja GUS](https://publikacje.new.stat.gov.pl/portal-publikacje/przecietne-zatrudnienie-i-wynagrodzenie-w-sektorze-przedsiebiorstw-we-wrzesniu-2026-r)
- **Kotwica.** Oba indeksy mają bazę 100 w tym samym miesiącu, wyznaczonym przed uruchomieniem serii. Kotwica pozostaje średnią geometryczną indeksów cen i płac. Pierwsze okno zaczyna od 100. Od kolejnego cyklu CPI łańcuchuje dynamiki po miesiącu bazowym.
- **Kalendarz.** Odcięcie o 12:00 24. dnia w strefie Europe/Warsaw. Jeżeli znamy wyłącznie datę publikacji, przyjmujemy początek następnego dnia jako udokumentowaną górną granicę czasu dostępności. Cykl 25. dnia dotyczy poprzedniego miesiąca i wyznacza wartości od 26. dnia do 25. dnia kolejnego miesiąca.
- **Ścieżka.** Od poprzedniej opublikowanej kotwicy `A_p` do nowej `A_n` stosujemy interpolację geometryczną `A_p × (A_n/A_p)^(k/K)`, gdzie `k = 1, …, K` i `K` to rzeczywista liczba dni okna. Dzień końcowy ma wartość `A_n`, a pierwsza zmiana kolejnego okna jest jego pierwszym krokiem dziennym. Obliczenia używają 40 cyfr precyzji pośredniej i wartości dziennych oraz kotwic zaokrąglonych do sześciu miejsc, z połówkami w górę.
- **Braki i rewizje.** Brak kwalifikującego się wejścia zatrzymuje cykl. Dni bez odczytu pozostają puste. Przy wznowieniu liczymy wszystkie brakujące mnożniki CPI od ostatniej kotwicy oraz aktualną dwunastomiesięczną średnią płac. Nowy odczyt obowiązuje wyłącznie w swoim przyszłym oknie. Zarchiwizowane obserwacje są wiążące. Zmiana definicji lub korekta skutkująca inną wartością wymaga nowej wersji i jawnej daty rozpoczęcia.

## Odtworzenie i testy

Każdy plik cyklu zawiera wejścia i ich skrót SHA-256, źródła i granicę dostępności każdej obserwacji, dzień cyklu, wartości, wersję i skrót kodu oraz skrót poprzedniego cyklu. Zapis tworzy plik wyłącznie raz, a ponowienie z tymi samymi wejściami zwraca istniejący wynik. Kolejny cykl wymaga weryfikacji zapisanej historii. Skrót ostatniego cyklu należy utrwalać niezależnie w Git podczas pilotażu i późniejszego wdrożenia. Lokalne sprawdzenie całego łańcucha bez zapisanego wcześniej skrótu końca nie wykryje obcięcia jego ogona przez usunięcie plików.

Próba bazowa z oficjalnych publikacji GUS za wrzesień 2026 r. używa CPI 100,7 i 12 wynagrodzeń z kolumny B tabeli 19. Średnia to 9 288,128333 zł. Cykl próbny 25 października odtwarza odczyt bazy 100,000000. Tabela płac była podlinkowana przez GUS w zestawieniu miesięcznym. Pobrana wersja ma w dokumencie datę modyfikacji 22.10.2026 i SHA-256 `04ee610097cccb58b4e3d13d64f9475baa1eacdd8dead709c1518892afa8072c`. Przykład jest rekonstrukcją. Metadane pliku i data publikacji zestawienia nie rozstrzygają, kiedy ten konkretny plik trafił na serwer. [Dane testowe z odnośnikami](../prototyp/tests/fixtures/tip0003-gus-2026-09.json) · [Zestawienie GUS z 23.10.2026](https://ssgk.stat.gov.pl/Wynagrodzenia_i_swiadczenia_spoleczne.html)

Testy przypadków brzegowych sprawdzają ciągłość dla ścieżki 100 → 110 → 110, luty przestępny, granicę odcięcia z przesunięciem czasu letniego, odmowę użycia późnego i zrewidowanego wejścia, całe brakujące okno, wznowienie z pełnym ciągiem CPI oraz identyczne ponowienie i wykrywanie zmian w archiwum.

## Decyzja do podjęcia po próbie równoległej

Przeprowadzić cykl próbny na wejściach zapisanych przed rzeczywistym odcięciem i sprawdzić przejście do następnego okna. Zachować kopie regularnych publikacji źródłowych wraz z czasem pobrania. Sprawdzić odtworzenie cykli z czystej kopii oraz zastosowanie przy przerwie w dostępności danych. Po ocenie wyników ustalić z autorem status TIP, oznaczenie wersji i datę uruchomienia. Automatyzacja rozliczeniowa wymaga jeszcze powiązania zatwierdzonych wejść z uruchomieniem, trwałego zapisu czasu faktycznej publikacji i uruchomienia wyłącznie dla zatwierdzonej wersji. Dotychczasowa historia pozostaje dostępna pod odrębnym oznaczeniem.
