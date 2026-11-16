# Talent polski — plan kontynuacji

Stan na 16 listopada 2026 r.

Rozwijamy dobrowolną regułę waloryzacji umów w PLN dla osób prywatnych i przedsiębiorstw. Bazą dalszych prób jest średnia geometryczna zmian polskich cen i płac z równymi wagami. Jawne źródła i z góry ustalona reguła mają pozwolić obu stronom samodzielnie sprawdzić należną kwotę. Ocena skutków dla konkretnej umowy wymaga danych o budżecie i kosztach jej stron.

## 1. Jedna faktura i pierwszy ekran strony

- Opracować fakturę z jedną odroczoną płatnością. Jeżeli dostępny jest rzeczywisty przypadek do wykorzystania, zanonimizować go. W razie braku danych użyć jasno oznaczonego scenariusza modelowego.
- Porównać nominał, CPI i Talent przy tych samych warunkach. Pokazać końcowe kwoty, udział płatności w budżecie kupującego i środki, które pozostają sprzedawcy po pokryciu kosztów. Podać źródła i założenia pozwalające powtórzyć obliczenie.
- Otworzyć stronę tym przypadkiem i pytaniem o to, co dzieje się z płatnością, gdy ceny i płace zmieniają się w różnym tempie. Z przykładu prowadzić do kalkulatora i whitepaperu. Sprawdzić, czy czytelnik spoza projektu rozumie cel reguły i potrafi odczytać kwoty.
- Jeżeli powstanie propozycja klauzuli umownej, poddać ją osobnej weryfikacji prawnej przed wykorzystaniem w umowie.

Punkty odniesienia do opracowania przykładu to [whitepaper](strona/whitepaper.md), [badanie wag i przykład roczny z GUS](materialy/walidacja_wag_talenta.md) oraz [przypadki kontrolne kalkulatora](prototyp/README.md#kalkulator-waloryzacji).

## 2. Pilotaż i niezależne odtworzenie TIP-0003

- Uzupełnić [plik listopadowej próby](prototyp/data/manual/tip0003-proba-2026-11-25.json) o regularny odczyt płac GUS za październik. Zachować dokładne kopie źródeł i udokumentować czas ich dostępności przed odcięciem. Kalendarz i polecenia są w [instrukcji przygotowania cyklu](INSTRUKCJA_aktualizacji.md#przygotowanie-cyklu-25-listopada-2026-r).
- Przeprowadzić dwa kolejne cykle na danych z rzeczywistych odcięć w odrębnej serii próbnej. Utrwalić skróty cykli poza archiwum wynikowym, sprawdzić przejście ścieżki między oknami oraz weryfikację z czystej kopii. Przećwiczyć też brak odczytu i wznowienie po przerwie.
- Poprosić niezależną osobę o odtworzenie kotwic i kwoty przykładowej płatności ze źródeł i opisu reguły w jej własnym arkuszu. Zapisać rozbieżności razem z danymi, wersją reguły i poziomem zaokrąglenia.
- Po pilotażu podjąć decyzję o wersji rozliczeniowej, dacie wejścia i integracji z publikacją. Powiązać konkretne wejścia z czasem faktycznej publikacji. Określić zasady braków i rewizji, ochronę historii oraz sposób oznaczenia wersji w kalkulatorze. Uzgodnić kod, politykę danych i instrukcję. [TIP-0003](TIP/TIP-0003-tln-pln-prospektywny.md) · [Audyt wcześniejszych kotwic](materialy/audyt_kotwic_2026.md)

## 3. Pytania badawcze po pilotażu

- Porównać obliczenia na pierwszych odczytach i na danych później zrewidowanych, gdy zbierze się archiwum cykli. Zbadać też wpływ opóźnień i wygładzania płac na płatności. Ocenić warianty wskaźnika płacowego z TIP-0001 i TIP-0002 na danych dostępnych w chwili rozliczenia. [Procedura TIP](TIP/README.md)
- Wyjaśnić łącznik szeregu wynagrodzeń przy zmianie definicji w 1999 r. i sprawdzić wrażliwość wyników na porównywalną dynamikę potwierdzoną u źródła. [Audyt danych](materialy/audyt_kotwic_2026.md)
- Rozszerzyć ocenę płynności na rzeczywiste przepływy gospodarstwa lub firmy. Potem sprawdzić pożyczkę ratalną, z rzeczywistym kosztem finansowania i warunkami obu stron. Do oceny niewypłacalności potrzebny jest odrębny model i dane o zobowiązaniach. [Dotychczasowa walidacja](materialy/walidacja_talent_pl.md)
- Ocenić, czy waloryzacja zmienia potrzebę zabezpieczenia walutowego u polskiego importera lub eksportera. Porównać tę samą ekspozycję, walutę, termin i przepływy. Uwzględnić premię za opcję, pozostałe koszty i ryzyko po obu stronach, również w scenariuszach skrajnych.

Talenty zagraniczne, konstrukcje wielostronne i AUV pozostają tematami odłożonymi.
