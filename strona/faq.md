# Najczęstsze pytania o Talenta

## Czym jest Talent i dla kogo powstaje?

Talent to propozycja wspólnego, dobrowolnie przyjmowanego standardu rozliczania umów dla osób prywatnych i przedsiębiorstw. Polski prototyp opiera się na krajowych cenach i przeciętnych wynagrodzeniach, a płatność jest określana w PLN. Jako pierwsze zastosowania badamy pożyczkę i płatność odroczoną. [Wprowadzenie](wprowadzenie.md)

## Od czego zależy kwota spłaty?

Mnożnik waloryzacji jest średnią geometryczną zmian cen i przeciętnych płac. Gdy płace rosną szybciej od cen, kwota indeksowana rośnie szybciej niż CPI. Połowa realnego wzrostu płac oznacza tu połowę zmiany **logarytmicznej**. Wzór wyznacza waloryzację kwoty. Odsetki i opłaty, jeśli występują, są odrębnymi elementami warunków umowy. [Wzór i dowód](whitepaper.md)

## Czy któraś ze stron może ponieść stratę?

Tak. Gdy ceny rosną szybciej niż płace, rośnie obciążenie względem przeciętnego wynagrodzenia i spada siła nabywcza spłaty względem CPI. Symetria dotyczy ilorazów przyjętych w modelu. Sytuacja konkretnego dłużnika lub wierzyciela zależy także od jego dochodów, kosztów i płynności.

## Jakie wyniki dały testy historyczne?

W polskiej próbie z lat 1989–2024 maksimum projektowej miary żalu wyniosło 10,4% dla horyzontów 3, 5, 10, 20 i 30 lat, przy założeniach historycznego szeregu płac. Roczne poziomy zweryfikowano w GUS, a porównywalność przy zmianie definicji w 1999 r. wymaga dalszej weryfikacji. W próbie USA z tymi samymi horyzontami uzyskano 6,1% dla CPI i płac z lat 1939–2025 oraz 19,7% dla CPI i PKB na osobę z lat 1929–2025. Wyniki dotyczą symulacji opartych na danych historycznych. [Raport polski](../materialy/wyniki_kruche_gospodarki.md) · [Raport USA](../materialy/wyniki_test_stulecia_usa.md)

## Jak projekt radzi sobie z brakami danych i silną inflacją?

Aktualizator korzysta z jednego źródła CPI. Przy jednym brakującym miesiącu może przenieść ostatnią znaną dynamikę, a przy drugim kolejnym braku przerywa aktualizację. Silną zmianę kotwicy oznacza flagą. Porównania alternatywnych źródeł, publikacja dekadowa i koszyk awaryjny pozostają propozycjami. CPI i HICP Polski korzystają częściowo z tych samych danych, więc ich porównanie ma ograniczoną wartość przy wykrywaniu błędów źródłowych. [Reguła publikacyjna](regula_publikacyjna.md)

## Co można zweryfikować samodzielnie?

Publiczny kod pozwala sprawdzić, jak wynik zależy od wejść. Pełne odtworzenie publikacji wymaga także dokładnych migawek danych i wersji kodu. Archiwum wiążące te elementy z każdym odczytem pozostaje do zbudowania. [Weryfikacja obliczeń](../dla_agenta.html)

## Co strony musiałyby uzgodnić w umowie?

Przykładowa konstrukcja wiąże zmianę kwoty w PLN z ilorazem dwóch odczytów TLN-PLN. Wymaga wskazania serii, wersji reguły, dat i postępowania w razie braku odczytu. Publikowane wartości mają charakter badawczy, a dzienny szereg jest demonstracją. Wzorzec klauzuli i jego weryfikacja prawna są osobnymi pracami.
