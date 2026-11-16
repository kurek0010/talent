# Ceny i płace w umowie — porównanie wag

**16 listopada 2026 r.** Siedem reguł waloryzacji porównaliśmy na tych samych historycznych harmonogramach faktur i pożyczek. Przy równych wagach średnia geometryczna i arytmetyczna dają bardzo zbliżone wyniki w krótszej próbie opartej na dochodach GUS. Zmiana udziału cen lub płac ma większe znaczenie. W symulacji wpływa na to, która strona i w ilu przypadkach potrzebuje dodatkowego finansowania.

## Co porównaliśmy

Punkty odniesienia to kwota nominalna, sam CPI i same płace. Do Talenta dodaliśmy średnią arytmetyczną 50/50 oraz średnie geometryczne 25/75 i 75/25. Pierwsza liczba oznacza wagę cen, druga wagę płac. Dla mnożników cen i płac liczonych od początku umowy średnia arytmetyczna to `(C + W)/2`, a geometryczna z wagą cen `a` to `C^a × W^(1−a)`. W badaniu liczymy średnią arytmetyczną bezpośrednio od początku danej umowy do każdej raty. Można też zbudować osobny indeks arytmetyczny o stałej bazie i dzielić jego poziomy. To inna reguła, z udziałem cen i płac w zmianie między datami zależnym od ich poziomów w chwili startu umowy.

Każde okno ma ten sam kapitał 100 000 zł i trzy harmonogramy. Faktura jest płatna w całości na końcu. Pożyczkę spłacamy w rocznych ratach z równym kapitałem, bez odsetek lub z 5% odsetek od pozostałego kapitału w jednostce bazowej. Waloryzujemy całą wymagalną kwotę, bez opłat. W pełnej próbie uwzględniamy po 615 okien na harmonogram w latach 1989–2024, o długości od 1 do 30 lat. Dane o cenach pochodzą z serii CPI OECD/FRED, a o wynagrodzeniach z GUS. Przejście przez 1999 r. korzysta z przybliżonego łącznika płac. [Metoda, źródła i pierwotna walidacja](walidacja_talent_pl.md)

W drugiej próbie budżet dłużnika podąża za **przeciętnym dochodem rozporządzalnym na osobę według GUS**. Liczymy 51 identycznych okien raz z budżetem opartym na płacach, raz z budżetem opartym na dochodzie. Omijamy przejście 2020–2021, ponieważ GUS zmienił podstawę uogólniania wyników. Okna mieszczą się w blokach 2011–2020 i 2021–2024. Każda metoda waloryzacji nadal używa tych samych danych cen i płac co poprzednio. [GUS, *Budżety gospodarstw domowych w 2024 r.*, wykres 1 i przypis, s. 26](https://stat.gov.pl/files/gfx/portalinformacyjny/pl/defaultaktualnosci/5486/9/23/1/budzety_gospodarstw_domowych_2024.pdf)

Mierzymy najwyższą płatność w relacji do budżetu lub dochodu, wartość realną wpływów i największą lukę gotówkową po wykorzystaniu rezerwy oraz nadwyżek z wcześniejszych rat. Na pożyczkę dostępne jest 25% modelowego dochodu, a na fakturę cały odłożony budżet. Bazowy koszt lub planowany wypływ wierzyciela wynosi 90% płatności bazowej w realnych złotych. Sprawdzamy osobno dochód o 25% niższy, koszty o 20% wyższe oraz oba szoki z rezerwą 5% lub 15% kapitału. Dane GUS opisują przeciętne gospodarstwo, a rezerwy, wydatki stron i terminy są założeniami symulacji. W fakturze ścieżka dochodu GUS sprawdza wrażliwość budżetu kupującego. Ocena przedsiębiorstwa wymagałaby jego rzeczywistych wpływów i kosztów.

## Wyniki

**Talent daje najmniejsze maksymalne odchylenie według miary z whitepaperu.** W pełnej próbie największy „żal” wyniósł 17,43% dla Talenta, 18,95% dla średniej arytmetycznej i 27,26% dla każdej z nierównych wag. Te wartości są takie same dla faktury i rat, ponieważ w każdym harmonogramie występuje okres z największą rozbieżnością cen i płac. Do oceny płynności używamy osobnej miary. [Definicja żalu w whitepaperze](../strona/whitepaper.md)

**W oknach z danymi o dochodzie GUS obie średnie 50/50 były do siebie zbliżone.** Przykładowo przy ratach 5% mediana najwyższego obciążenia w umowie wyniosła 37,84% dochodu dla Talenta i 37,85% dla średniej arytmetycznej. Mediana realnych wpływów wierzyciela to odpowiednio 103,82% i 103,91% wartości harmonogramu bazowego. Przy przeciętnym dochodzie GUS faktura 2021–2022 oparta na Talencie pochłania 101,13% modelowego budżetu kupującego, wobec 101,05% przy budżecie zmieniającym się tak jak płace. Realna wartość wpływu sprzedawcy w obu przypadkach to 98,96% kwoty bazowej.

**Najmniejsza skrajna luka zależy od umowy, zakresu próby i założeń o dochodzie.** Poniżej największa luka którejkolwiek ze stron w badanych oknach przy obu szokach i rezerwie 5%. Kwoty podano w złotych o sile nabywczej z początku umowy, zaokrąglone do pełnego złotego. Maksima dla różnych metod mogą przypadać w innych oknach.

| Reguła | Faktura, pełna próba | Raty 5%, pełna próba | Faktura, dochód GUS | Raty 5%, dochód GUS |
| --- | ---: | ---: | ---: | ---: |
| Nominał | 102 084 | 181 897 | 27 501 | **81 361** |
| CPI | 40 614 | 86 019 | 21 604 | 81 651 |
| Płace | 59 283 | 92 892 | 26 341 | 89 316 |
| Talent 50/50 | 25 770 | 85 581 | **20 895** | 83 846 |
| Arytmetyczna 50/50 | 26 871 | 85 806 | 20 904 | 83 975 |
| Geometryczna 25/75 | **24 419** | 89 179 | 21 964 | 86 548 |
| Geometryczna 75/25 | 32 894 | **82 096** | 21 085 | 81 886 |

- **Częstość i wielkość luki mogą prowadzić do różnych wyborów.** W pełnej próbie rat 5% waga 75/25 obniża największą lukę którejkolwiek ze stron z 85 581 do 82 096 zł względem Talenta. Jednocześnie luka wierzyciela pojawia się w 57,72% okien wobec 24,88% dla Talenta. W próbie 51 okien z dochodem GUS nominał ma najniższą skrajną lukę przy ratach 5%, lecz luka wierzyciela występuje w 100% okien wobec 49,02% dla Talenta. To odsetki symulowanych okien, często nakładających się na siebie.
- **Krótkie umowy mogą przesądzać o maksimum.** Gdy w pełnej próbie ograniczymy początki umów do lat od 1999 r. i horyzonty do 5–30 lat, w tym samym scenariuszu najniższą skrajną lukę daje CPI dla obu harmonogramów. Dla faktury jest to 14 890 zł wobec 18 241 zł w Talencie, a dla rat 5% odpowiednio 12 617 i 14 763 zł. W tej próbie jest po 231 okien na harmonogram.
- **Sposób liczenia średniej ma znaczenie przy dzieleniu okresu.** Jeśli ceny najpierw się podwoją, a potem spadną o połowę przy stałych płacach, średnia arytmetyczna mnożników dla dwóch osobnych okresów daje po przemnożeniu 1,125. Obliczona wprost od początku do końca daje 1. Średnia geometryczna daje 1 w obu przypadkach. To własność wzoru niezależna od symulacji płynności.

## Odtwórz obliczenie z komunikatów GUS

Załóżmy jedną płatność bazową **10 000 zł** i roczną regułę przykładową v1. Porównujemy średnie za lata 2021 i 2022 według komunikatów dostępnych na **1 marca 2023 r.** Do tego rachunku bierzemy roczny CPI ogłoszony bezpośrednio przez GUS. Symulacja historyczna korzysta z poziomów CPI z szeregu OECD/FRED, a miesięczny prototyp ma własny kalendarz i szeregi wejściowe.

| Wejście | Odczyt | Data komunikatu | Źródło |
| --- | ---: | --- | --- |
| Średnioroczny CPI w 2022 r. (2021 = 100) | 114,4 | 13.01.2023 | [M.P. 2023 poz. 68](https://eli.gov.pl/eli/MP/2023/68/ogl) |
| Przeciętne wynagrodzenie w gospodarce narodowej w 2021 r. | 5 662,53 zł | 09.02.2022 | [M.P. 2022 poz. 175](https://eli.gov.pl/eli/MP/2022/175/ogl) |
| Przeciętne wynagrodzenie w gospodarce narodowej w 2022 r. | 6 346,15 zł | 09.02.2023 | [M.P. 2023 poz. 171](https://eli.gov.pl/eli/MP/2023/171/ogl) |

Mnożnik cen to 114,4 ÷ 100 = 1,144. Mnożnik płac to 6 346,15 ÷ 5 662,53. Mnożymy 10 000 zł przez pierwiastek z iloczynu tych dwóch mnożników i zaokrąglamy dopiero końcową kwotę do grosza. Otrzymujemy **11 323,04 zł**. Wartości z komunikatów i wszystkie formuły są zapisane w [arkuszu kontrolnym](odtworzenie-talenta-2021-2022.xlsx).

## Odtwórz badanie

W katalogu repozytorium uruchom Python 3.10 lub nowszy. Skrypt wypisuje tabele i opcjonalnie zapisuje 75 285 wierszy CSV z wynikami wszystkich harmonogramów, scenariuszy i reguł. Ścieżka wyjściowa musi wskazywać nowy plik. Dane potrzebne do obliczeń są w repozytorium.

```bash
python3 prototyp/src/walidacja_wag.py --csv wyniki-wag.csv
```

[Kod porównania](../prototyp/src/walidacja_wag.py) · [Model przepływów](../prototyp/src/walidacja_pl.py)
