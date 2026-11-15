# Instrukcja miesięcznej aktualizacji Talenta (dla Claude Code / administratora)

**Stan dokumentacji:** 2026-11-15. Instrukcja opisuje miesięczne odczyty badawcze TLN-PLN. [Reguła publikacyjna](strona/regula_publikacyjna.md) · [Polityka danych](POLITYKA_danych_v0.1.md)

Od 25. dnia miesiąca aktualizator oczekuje kotwicy za poprzedni miesiąc. Planowane odcięcie wejść 24. dnia o 12:00 wymaga archiwum dat dostępności danych. Workflow nie generuje szeregu dziennego.

Aktualizator wykorzystuje listę miesięcy z `talent_published.json` i dopisuje kotwice po ostatnim zapisanym miesiącu. Zasada zachowania historii obejmuje cały projekt, a rejestr samych miesięcy nie zabezpiecza przed nadpisaniem plików przez inny skrypt. `talent_daily.py` zapisuje wyniki demonstracji w `prototyp/data/research/`.

Przy ręcznym uzupełnianiu danych aktualne wejścia zapisuje się w `prototyp/data/first_prints_pln.json` z oznaczeniem źródła. Płace roczne są interpolowane między punktami lipcowymi. Dane oznaczone jako proxy i wartości z przeniesionej dynamiki CPI wymagają odnotowania przy weryfikacji wyniku. Warianty TIP-0001 i TIP-0002 pozostają poza aktywną ścieżką.

## Automatyzacja

**Włączony w repozytorium od 2026-07-09.** GitHub Action `.github/workflows/publikacja_kotwicy.yml`,
cron `0 9 25 * *` (25. dnia miesiąca, 09:00 UTC):

1. `prototyp/src/fetch_gus.py` — pobiera dynamiki CPI m/m z tabeli GUS
   „Miesięczne wskaźniki cen… od 1982 roku" (bieżący CSV),
   append-only do `prototyp/data/first_prints_pln.json`. Płace roczne (komunikat
   Prezesa GUS) — próba automatyczna tylko w lutym, inaczej zgłasza potrzebę
   ręcznego wpisu.
2. `prototyp/src/talent_update.py` — czyta z `first_prints_pln.json`, liczy nowe
   kotwice (dopisuje po ostatniej kotwicy z rejestru `talent_published.json`).
   Kaskada awaryjna: 1 brakujący miesiąc CPI = carry-forward ostatniej dynamiki
   + alert; 2 kolejne braki = przerwanie **bez** publikacji (Issue w repo).
3. `prototyp/src/update_fx.py` — uzupełnia przeliczenia na podstawie kursów NBP, po czym `prototyp/src/build_strona.py` przebudowuje stronę.
4. Commit (`github-actions[bot]`) i push — **tylko gdy są nowe kotwice**;
   komunikat: `Kotwica TLN-PLN za YYYY-MM: <wartość>` + alerty.

**Ręczne uruchomienie:** zakładka Actions → „Publikacja kotwicy TLN-PLN" →
Run workflow (opcjonalnie zaznacz `dry_run`, żeby zobaczyć podgląd zmian bez
commita/pusha).

**Wyłączenie:** zakładka Actions → „Publikacja kotwicy TLN-PLN" → „…" →
Disable workflow. Albo usuń/zakomentuj blok `schedule:` w pliku workflow
(zostanie tylko ręczne uruchamianie przez `workflow_dispatch`).

**Błąd/alert automatu** → automat tworzy Issue w repozytorium z logiem i
instrukcją, co ma zrobić człowiek (zwykle: ręczny wpis do
`first_prints_pln.json`, potem ponowne ręczne uruchomienie).

**Drugi automat — przebudowa strony po zmianie treści.** GitHub Action
`.github/workflows/przebudowa_strony.yml` (działa od 2026-07-12): trigger to
push na `main`, który zmienia jeden z plików `.md` kompilowanych na stronę
(dokładnie klucze słownika `DOCS` w `build_strona.py`) albo
`prototyp/src/strona_szablon.html`/`prototyp/src/build_strona.py`. Uruchamia
wyłącznie `build_strona.py` i commituje wygenerowane HTML (autor
`github-actions[bot]`, komunikat `Przebudowa strony po zmianie treści`) —
tylko jeśli builder faktycznie coś zmienił. Dokumenty spoza słownika `DOCS`
(`materialy/SZKIC_`, `materialy/TALENTY_`, `materialy/waluty/` itd.) nie są na liście
`paths` i push do nich nie uruchamia builda. **Dodajesz plik do `DOCS`** →
dopisz go też do `paths` w tym workflow, inaczej treść się zmieni, ale strona
nie. Wyłączenie: zakładka Actions → „Przebudowa strony po zmianie treści" →
„…" → Disable workflow.

## Przeliczenia walutowe

Wartości w innych walutach to przeliczenia polskiej kotwicy. Wersje oparte na danych innych gospodarek pozostają programem dalszych badań.

## Próba prospektywna TIP-0003

[TIP-0003](TIP/TIP-0003-tln-pln-prospektywny.md) definiuje metodę, która jest obecnie testowana w odrębnej serii. Komenda próbna zapisuje tylko do `prototyp/data/prospektywny-test/`. Seria publiczna korzysta z dotychczasowego workflow.

1. Dla cyklu z 25. dnia wybierz dane dostępne przed odcięciem w południe dnia 24. Zachowaj źródłowe pliki GUS i czas pobrania. W JSON wpisz obiekty `cpi` i `wages` z kluczami `YYYY-MM`. Każda obserwacja zawiera `value` jako tekst dziesiętny, `source` jako adres komunikatu GUS oraz `available_by` jako najpóźniejszy udokumentowany czas dostępności z przesunięciem strefy czasowej.
2. Przekaż 12 kolejnych poziomów płac, kończąc na miesiącu kotwicy. Zachowuj te same obserwacje w nakładających się oknach. W pierwszym cyklu podaj jedną obserwację CPI dla miesiąca bazowego. W następnym podaj CPI dla wszystkich miesięcy między ostatnią zatwierdzoną kotwicą a nową, wyłącznie z wartościami nowymi dla łańcucha.
3. W katalogu repozytorium uruchom `python3 prototyp/src/talent_prospective.py test WEJSCIA.json --cycle RRRR-MM-25`, a następnie `python3 prototyp/src/talent_prospective.py verify`. Zachowaj z plikiem cyklu wynikowy skrót ostatniego rekordu, konkretną wersję kodu i źródła. Przy odtwarzaniu użyj kodu o tym samym skrócie i przekaż niezależnie zapisany skrót ostatniego cyklu do `verify --expected-sha256 SKRÓT`.
4. Przy kwalifikujących się danych brakujących dla cyklu wznów w następnym przyszłym oknie, gdy dostępny jest pełny ciąg CPI. W okresie przerwy wynik pozostaje brakujący. Przygotowanie rozliczeniowego workflow i jawnej daty startu wymaga decyzji po pilotażu.

Przykład wejścia i odczytu bazowego opisuje [test TIP-0003 na danych GUS](prototyp/tests/fixtures/tip0003-gus-2026-09.json).

### Przygotowanie cyklu 25 listopada 2026 r.

[Plik listopadowej próby](prototyp/data/manual/tip0003-proba-2026-11-25.json) zawiera regularny CPI 99,6 oraz 11 poziomów płac od listopada 2025 do września 2026 r. z [tablicy 19 GUS](https://bazydanych.new.stat.gov.pl/file/199294/download). Październikowe wynagrodzenie pozostaje do uzupełnienia po regularnej publikacji GUS. [Komunikat CPI](https://stat.gov.pl/obszary-tematyczne/ceny-handel/wskazniki-cen/wskazniki-cen-towarow-i-uslug-konsumpcyjnych-w-pazdzierniku-2026-r-%2C2%2C180.html)

1. Zapisz źródłową tabelę płac i komunikat CPI wraz z czasem pobrania. W kopii pliku wejściowego dodaj `wages["2026-10"]` z kwotą brutto dla sektora przedsiębiorstw ogółem, linkiem i udokumentowanym `available_by`. Odcięcie to **24 listopada, godz. 12:00 czasu polskiego**. Przy zapisie opartym tylko na dacie publikacji, odczyt z 24 listopada wymaga także potwierdzenia dostępności do południa.
2. Gdy wszystkie wejścia są udokumentowane, 25 listopada uruchom próbę na osobnej serii w katalogu roboczym:

   ```bash
   python3 prototyp/src/talent_prospective.py test /tmp/tip0003-listopad-uzupelniony.json --cycle 2026-11-25
   python3 prototyp/src/talent_prospective.py verify
   ```

3. Zapisz skrót cyklu poza katalogiem wynikowym i potwierdź odtworzenie za pomocą `verify --expected-sha256`. Pierwsza próba w pustym archiwum ustala bazę 100. Zmianę między oknami można sprawdzić w kolejnym rzeczywistym cyklu. Przy niekompletnym wejściu skrypt pozostawia próbę bez odczytu.
