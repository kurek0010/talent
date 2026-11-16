# Talent — reguła waloryzacji dla umów rozliczanych w PLN

Talent to propozycja wspólnego standardu rozliczania umów dla osób prywatnych i przedsiębiorstw. W rozwijanej obecnie polskiej wersji opiera się na otwartej regule waloryzacji, która według uzgodnionej wcześniej zasady dzieli między strony wpływ zmian cen i przeciętnych wynagrodzeń. Przyjęcie reguły jest dobrowolne. Obecny zakres to polska gospodarka i rozliczenia w PLN.

Jawność reguły, danych i obliczeń ma umożliwiać niezależne odtworzenie wyniku oraz ocenę skutków przyjętej zasady. Projekt pozostaje prototypem badawczym. Jego zastosowania i ograniczenia są przedmiotem weryfikacji.

## 1. Problem i założenia

W pożyczce lub umowie z odroczoną płatnością strony mogą uzgodnić, jak zmieni się kwota w PLN między zawarciem umowy a zapłatą. Przy wzroście cen spłata nominalna ma mniejszą siłę nabywczą. Indeksacja CPI zachowuje relację kwoty do koszyka konsumpcyjnego, a indeksacja płacami zachowuje relację do przeciętnego wynagrodzenia. Gdy ceny i płace zmieniają się w różnym tempie, tych dwóch relacji nie można jednocześnie zachować.

**Założenie modelu.** CPI jest punktem odniesienia dla wierzyciela, a przeciętne wynagrodzenie dla dłużnika. Odpowiadają one za porównywalność kwoty względem koszyka cen i przeciętnej płacy. Przeciętna płaca może się zmieniać inaczej niż płaca lub dochód konkretnego kontrahenta. CPI może się zmieniać inaczej niż koszty produkcji konkretnego przedsiębiorstwa.

Uczciwość oznacza tutaj świadomą zgodę obu stron na jawną zasadę podziału skutków zmian gospodarczych, zanim te zmiany nastąpią. Symetria obu punktów odniesienia jest wyborem projektowym.

## 2. Definicja indeksu i metryki

Dla dodatnich indeksów cen \\(C(t)\\) i płac \\(W(t)\\) indeks bazowy Talenta wynosi

$$T(t) = 100 \cdot \sqrt{\frac{C(t) \cdot W(t)}{C(0) \cdot W(0)}}.$$

Rozważmy pojedynczą płatność. Niech \\(R\\) będzie ilorazem kwoty końcowej i początkowej w PLN, a \\(C\\) i \\(W\\) ilorazami poziomów cen i płac między tymi samymi datami. Waloryzacja Talentem daje \\(R=\sqrt{CW}\\). Iloraz indeksu między dwiema datami jest niezależny od wyboru bazy, a ilorazy dla kolejnych okresów można mnożyć.

## 3. Dlaczego średnia geometryczna?

Jeśli ceny rosną o 20%, ich mnożnik wynosi 1,20. Jeśli potem spadają o 10%, mnożymy przez 0,90. Po obu zmianach otrzymujemy 1,20 × 0,90 = 1,08, czyli wzrost o 8%. Tak samo mnożą się kolejne zmiany płac. Chcemy, żeby waloryzacja działała według tej samej zasady.

Przyjmujemy trzy warunki.

1. **Zgodność.** Gdy ceny i płace zmieniają się o tyle samo, kwota umowy zmienia się o tyle samo.
2. **Symetria.** Zamiana tempa wzrostu cen i płac daje taką samą kwotę. Przykładowo wzrost cen o 20% i płac o 10% daje taki sam wynik jak wzrost cen o 10% i płac o 20%. Równe traktowanie obu wskaźników to założenie tej reguły.
3. **Spójność w czasie.** Przy tych samych danych i tej samej regule możemy policzyć zmianę od razu za cały okres albo przemnożyć wyniki z kolejnych odcinków. Przykładowo podział roku na dwa półrocza daje ten sam mnożnik roczny przed zaokrągleniem płatności.

Wyobraźmy sobie dwa kolejne okresy. W pierwszym ceny mnożą się przez \\(C\\), a płace przez \\(W\\). W drugim zamieniamy te mnożniki miejscami. Po obu okresach zarówno ceny, jak i płace zmieniły się przez ten sam łączny mnożnik \\(CW\\), więc zgodnie z pierwszym warunkiem kwota umowy też musi zmienić się przez \\(CW\\).

Z symetrii wynika, że Talent ma dać w każdym z tych okresów taki sam mnożnik \\(R\\). Spójność w czasie mówi, że trzeba te dwa wyniki pomnożyć. Dostajemy \\(R \times R = CW\\). Jedyna dodatnia liczba spełniająca ten warunek to \\(R = \sqrt{CW}\\). Ten wzór spełnia wszystkie trzy warunki dla dowolnych dodatnich mnożników cen i płac.

Jeśli ceny rosną o 20%, a płace o 10%, mnożnik Talenta wynosi \\(\sqrt{1{,}20 \times 1{,}10} \approx 1{,}1489\\). Płatność w wysokości 10 000 zł wzrosłaby do około 11 489 zł. Jeśli później ceny i płace wrócą dokładnie do poziomów wyjściowych, waloryzacja za cały okres da z powrotem 10 000 zł.

Ten sam rachunek można powtórzyć na rzeczywistych danych. W przykładzie dla lat 2021–2022 z trzech komunikatów GUS i kwoty 10 000 zł otrzymujemy 11 323,04 zł. [Dane, daty i arkusz do samodzielnego przeliczenia](../materialy/walidacja_wag_talenta.md)

### Literatura i przykłady zastosowań

- **Jak łączyć wskaźniki.** William Stanley Jevons stosował średnią geometryczną do zmian cen poszczególnych towarów. Irving Fisher użył jej do połączenia dwóch indeksów cen. Podręcznik MFW pokazuje, jak w przypadku Fishera wybór wzoru wiąże się z symetrią i odwróceniem kolejności okresów. Są to przykłady uzasadniania wzoru przez własności, które ma spełniać. [Jevons (1865)](https://www.jstor.org/stable/2338419) · [Fisher (1922)](https://www.loc.gov/resource/gdcmassbookdig.makingofindexnum00fish/?sp=1&st=grid) · [MFW, *Consumer Price Index Manual: Theory*, rozdz. 2 i 6](https://www.imf.org/en/-/media/files/publications/manuals-and-guides/2025/english/cpimea2025.pdf)
- **Co może być podstawą rozliczenia umowy.** Robert Shiller zaproponował dla USA dwie odrębne jednostki rozliczeniowe, jedną powiązaną z CPI, a drugą z dochodem na osobę skorygowanym o trend. Tę drugą wskazał m.in. jako możliwą podstawę spłat hipotecznych. Z Ryanem Schneiderem badał też, jak zmieniają się dochody różnych grup pracowników. [Shiller (1998)](https://www.nber.org/papers/w6356) · [Shiller i Schneider (1998)](https://www.nber.org/papers/w5254)
- **Jak łączyć ceny z płacami w praktyce.** Szwajcarski system emerytalny AHV stosuje średnią arytmetyczną indeksu cen i indeksu płac. Pokazuje to inne zastosowanie koncepcji równych wag i daje punkt odniesienia do porównania z Talentem. [Szwajcarski Federalny Urząd Ubezpieczeń Społecznych, s. 8](https://www.bsv.admin.ch/dam/de/sd-web/ypOw79fQ2sDS/Aktualisierungspraxis%20BSV.pdf)
- **Jak wyznaczać wartości dzienne.** Bank Centralny Chile rozkłada miesięczną zmianę CPI na równe dzienne mnożniki w jednostce *Unidad de Fomento*. Urugwaj powiązał dzienną *Unidad Previsional* ze zmianami płac nominalnych. Chilijska metoda rozkładania zmiany w czasie jest bliska interpolacji testowanej w TIP-0003. [Bank Centralny Chile](https://si3.bcentral.cl/estadisticas/Principal1/Metodologias/EMF/UF_IVP.pdf) · [Urugwaj, ustawa 19.608](https://www.impo.com.uy/bases/leyes-originales/19608-2018)

## 4. Jak formuła rozkłada odchylenia od cen i płac

Dla pojedynczej płatności definiujemy projektowy żal (*regret*) jako dodatnie odchylenie od przyjętego punktu odniesienia. Dłużnik porównuje spłatę z płacami, a wierzyciel ceny ze spłatą.

$$J_D = \max(0,R/W-1), \qquad J_V = \max(0,C/R-1), \qquad J = \max(J_D,J_V).$$

Wzrost obciążenia względem płac wynosi \\(R/W-1\\). Zwykły procent utraty siły nabywczej wynosi \\(1-R/C\\), podczas gdy metryka wierzyciela używa odwrotnego ilorazu \\(C/R\\). Dlatego żal wierzyciela może przekroczyć 100%.

### Twierdzenie i dowód

**Twierdzenie.** Przy ustalonych \\(C>0\\) i \\(W>0\\) średnia geometryczna minimalizuje większy z dwóch tak zdefiniowanych żalów wśród dodatnich mnożników spłaty. Gdy \\(C>W\\), jest jedynym minimizatorem. Gdy \\(C\le W\\), minimum wynosi zero dla każdego \\(R\\) w przedziale od \\(C\\) do \\(W\\).

**Dowód.** Iloczyn \\((R/W)(C/R)=C/W\\) jest stały. Większy z dwóch dodatnich czynników jest co najmniej równy ich średniej geometrycznej, a równość zachodzi, gdy czynniki są równe. Dla \\(C>W\\) daje to \\(R=\sqrt{CW}\\) i \\(J=\sqrt{C/W}-1\\). Dla \\(C\le W\\) oba składniki żalu są zerowe wtedy i tylko wtedy, gdy \\(C\le R\le W\\).

Średnia geometryczna jest środkiem w skali logarytmicznej także w przedziale zerowego żalu. Jej wybór pozwala stosować tę samą symetryczną regułę niezależnie od tego, czy ceny wyprzedzą płace. Minimalizacja dotyczy określonej wyżej metryki i modelu pojedynczej płatności. Szkody indywidualne i skutki dla wypłacalności wymagają dodatkowych miar.

**Przykład.** Jeśli ceny wzrosną o 50%, a płace o 20%, mnożnik spłaty wyniesie \\(\sqrt{1{,}50\cdot1{,}20}\approx1{,}3416\\). Obciążenie względem przeciętnej płacy wzrośnie o 11,8%, a siła nabywcza spłaty spadnie o 10,6%. Zgodnie z definicją projektowy żal obu stron wyniesie 11,8%. Przy indeksacji samym CPI żal dłużnika wyniósłby 25%, a przy spłacie nominalnej żal wierzyciela wyniósłby 50%.

## 5. Wyniki historyczne i zakres prób

Testy obejmują wszystkie dostępne roczne daty startu dla wybranych horyzontów **3, 5, 10, 20 i 30 lat**. Symulują jedną płatność z prostą waloryzacją średnią geometryczną. Skrypty liczą żal w logarytmach i raportują go jako \\(100(e^j-1)\\). Kategoria „zero” w tabelach obejmuje wyniki poniżej 0,02 w logarytmach, czyli poniżej około 2,02% w skali raportu.

| Próba | Punkty odniesienia | Maksymalny żal w próbie |
|---|---|---|
| Polska 1989–2024 | CPI i zweryfikowane poziomy płac GUS z przybliżonym łącznikiem 1999 r. | 10,4% w latach 1989–1994 |
| USA 1939–2025 | CPI i płaca godzinowa pracowników produkcyjnych w przemyśle | 6,1% w latach 1978–2008 |
| USA 1929–2025 | CPI i nominalny PKB na osobę | 19,7% w latach 1929–1932 |

W amerykańskiej próbie płacowej rozszerzenie obliczeń na wszystkie całkowite horyzonty od 3 do 30 lat daje 7,06% w latach 1978–1993. Wyniki zależą od punktów odniesienia, lat i horyzontów. [Raport polski](../materialy/wyniki_kruche_gospodarki.md) · [Raport USA](../materialy/wyniki_test_stulecia_usa.md)

Testy roczne nie odtwarzają operacyjnej ścieżki z opóźnieniami, pierwszymi odczytami i brakami danych. Interpolacja rocznych płac użyta do rekonstrukcji miesięcznej może korzystać z informacji dostępnej dopiero później. [Archiwalne porównanie kandydatów, w tym AUV](../materialy/wyscig_kandydatow.md) korzystało z CPI USA i dochodu na osobę na świecie. [Eksperyment dwustronny PL–US](../materialy/wyniki_talent_dwustronny.md) stanowi dalszy temat badawczy.

## 6. Stan polskiego prototypu

Strona pokazuje miesięczne kotwice, czyli wartości indeksu przypisane do poszczególnych miesięcy. Aktywny aktualizator dopisuje je w oparciu o CPI GUS i interpolowane roczne przeciętne wynagrodzenia, z przenoszeniem ostatniej wartości składnika płacowego poza zakresem interpolacji. Obliczenia z funduszem płac i wygładzonym zatrudnieniem są propozycją badaną osobno.

Szereg dzienny jest demonstracją. Dotychczasowy wzór przedłuża ostatnią dynamikę i może powodować skoki między oknami. Miesięczny workflow nie aktualizuje tego szeregu. Projekt przyjmuje zasadę zachowania opublikowanej historii. Skuteczne powiązanie każdej kotwicy z jej wejściami, datą i wersją kodu pozostaje zadaniem wdrożeniowym. [Reguła publikacyjna](regula_publikacyjna.md) · [Specyfikacja](../specyfikacja.html)

## 7. Hipoteza ekonomiczna i plan badań

Podział skutków zmian cen i płac może ograniczyć nadmierne obciążenie jednego kontrahenta w kryzysie, co mogłoby pomóc utrzymać współpracę. Sprawdzenie tej hipotezy wymaga danych o przepływach i modelu niewypłacalności. Sam dowód minimizacji żalu nie rozstrzyga, czy strony będą mogły zapłacić w terminie.

W polskich próbach porównaliśmy kwotę nominalną, CPI, płace oraz cztery sposoby łączenia cen i płac na tych samych fakturach i pożyczkach. Średnie geometryczna i arytmetyczna 50/50 dały zbliżone wyniki w oknach, w których budżet dłużnika oparto na dochodach GUS. Najmniejsza skrajna luka gotówkowa zależała od rodzaju umowy, zakresu badania i założeń o budżecie. [Wyniki i kod do ich odtworzenia](../materialy/walidacja_wag_talenta.md)

Odtworzono kotwice z czerwca–września 2026 r. Trwają testy prospektywnej reguły opisanej w TIP-0003. Wersje dla innych gospodarek i rozliczenia wielostronne pozostają poza bieżącym zakresem.
