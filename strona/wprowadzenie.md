# Talent — propozycja standardu rozliczania umów

Talent to propozycja wspólnego standardu rozliczania umów dla osób prywatnych i przedsiębiorstw. W rozwijanej obecnie polskiej wersji opiera się na otwartej regule waloryzacji, która według uzgodnionej wcześniej zasady dzieli między strony wpływ zmian cen i przeciętnych wynagrodzeń. Strony przyjmują tę regułę dobrowolnie. Obecny zakres projektu to polska gospodarka i rozliczenia w PLN.

Jawność reguły, danych i obliczeń ma umożliwiać niezależne odtworzenie wyniku oraz ocenę skutków przyjętej zasady. Projekt pozostaje prototypem badawczym. Jego zastosowania i ograniczenia są przedmiotem weryfikacji.

## Co strony uzgadniają

Przy płatności odroczonej od ustalenia kwoty do zapłaty może minąć rok lub kilka lat. W tym czasie zmieniają się ceny i dochody. Niezmieniona kwota pozwala kupić mniej, jeżeli ceny wzrosły, i może stanowić inną część dochodu płacącego niż w dniu zawarcia umowy.

CPI, czyli wskaźnik cen towarów i usług konsumpcyjnych, pozwala porównać kwotę z ceną koszyka konsumpcyjnego. Przeciętna płaca daje drugi punkt odniesienia, którym jest relacja płatności do wynagrodzeń w gospodarce. Uczciwość oznacza tu przyjęcie przez obie strony jawnej zasady podziału skutków tych zmian, zanim nastąpią.

## Jak działa reguła

Talent przyjmuje średnią geometryczną mnożników wzrostu cen i płac. Jeśli ceny wzrosną o 20%, a płace o 10%, mnożnik wyniesie √(1,20 × 1,10) ≈ 1,1489. Początkowa kwota 10 000 zł wzrosłaby do około 11 489 zł. Przy stałej kwocie byłoby to 10 000 zł, a przy waloryzacji CPI 12 000 zł. W skali logarytmicznej Talent leży dokładnie w połowie między zmianą cen i płac.

CPI opisuje koszyk konsumpcyjny, a koszty produkcji konkretnej firmy mogą się zmieniać w innym tempie. Podobnie płaca przeciętna i dochód konkretnego kontrahenta mogą się rozchodzić. W kryzysie podział skutków uzgodniony z góry może ograniczyć obciążenie jednej ze stron i pomóc utrzymać współpracę. To hipoteza ekonomiczna wymagająca osobnego badania płynności i wypłacalności.

## Dwa zastosowania do sprawdzenia

- **Pożyczka.** Strony mogą uzgodnić waloryzację kwoty między wypłatą a spłatą. Przykład z jedną płatnością pozwala porównać skutki dla pożyczkodawcy i pożyczkobiorcy.
- **Płatność odroczona.** Przedsiębiorstwa mogą rozważyć taką regułę przy zapłacie za maszynę lub dostawę materiałów. Ocena wymaga porównania waloryzacji z kosztami dostawcy, przychodami odbiorcy i terminami przepływów.

Otwarte dane i kod ograniczają uznaniowość obliczeń. Ich odtworzenie sprawdza rachunek przy tych samych wejściach. Jakość statystyki publicznej i dobór wskaźników wymagają odrębnej oceny.

[Metoda, dowód i wyniki historyczne](whitepaper.md) · [Stan publikacji](regula_publikacyjna.md) · [Najczęstsze pytania](faq.md)
