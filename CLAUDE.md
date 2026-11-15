# Instrukcje dla agentów pracujących w tym repozytorium

## Architektura strony — ZASADA NADRZĘDNA

Wszystkie pliki HTML w korzeniu generuje **builder**: `prototyp/src/build_strona.py`.

**NIGDY nie edytuj bezpośrednio:** `index.html`, `talent_strona.html`, `whitepaper.html`, `wprowadzenie.html`, `faq.html`, `regula_publikacyjna.html`, `wyscig_kandydatow.html`, `wyniki_*.html`, `tip.html` — builder nadpisze te zmiany bez ostrzeżenia.

Zamiast tego edytuj źródła i uruchom builder:

| Chcesz zmienić | Edytuj | Potem |
|---|---|---|
| układ/treść strony głównej (w tym sekcję rynkową z kaflami i wykresem) | `prototyp/src/strona_szablon.html` | `cd prototyp && python src/build_strona.py` |
| treść dokumentów (whitepaper itd.) | źródło `.md`: artykuły witryny w `strona/`, strony dowodowe w `materialy/`, TIP w `TIP/` — nazwa pliku md odpowiada nazwie html (markdown jest kanoniczny) | j.w. |
| listę dokumentów konwertowanych na HTML lub podmiany linków wewnątrz nich | słowniki `DOCS` / `LINK_REWRITES` w `build_strona.py` | j.w. **+ dodaj plik też do `paths` w `.github/workflows/przebudowa_strony.yml`**, inaczej push nie przebuduje strony automatycznie |
| wykresy/dane na stronie | skrypty w `prototyp/src/` (aktualizują `data/processed/`) | j.w. |

Ręcznie utrzymywane strony HTML (wolno edytować): `specyfikacja.html`, `dla_agenta.html`.
Markery danych i kodu w szablonie (m.in. `__DATA__`, `__FX__`, `__CONTRACT_DATA__`, `__CONTRACT_SCRIPT__`) wypełnia builder. Logika kalkulatora waloryzacji jest w `prototyp/src/kalkulator_umowy.js` i trafia do wygenerowanego HTML.

## Zasady merytoryczne projektu (obowiązują też agentów)

1. **Kod jest metodologią.** Zmiany formuły Talenta wyłącznie przez proces TIP (`TIP/README.md`): nazwij problem → zaproponuj → przetestuj na danych → dopiero zmień regułę. Nigdy nie zmieniaj formuły „przy okazji".
2. **Nigdy wstecz.** Opublikowane wartości i wyniki raportów nie są przeliczane po cichu; poprawki wchodzą jako nowe wersje z uzasadnieniem.
3. **Dane wejściowe:** rejestr źródeł i kaskady awaryjne w `POLITYKA_danych_v0.1.md`. Migawki danych w `prototyp/data/raw/` mają charakter dokumentacyjny — nie nadpisuj ich bez odnotowania daty pobrania.
4. **Liczby w dokumentach** pochodzą z konkretnych skryptów (`regret_*.py`, `talent_daily.py` itd.) — zmieniając skrypt, sprawdź, które dokumenty cytują jego wyniki.
5. `prototyp/.env` zawiera klucz API — nigdy nie commitować (jest w .gitignore).

## Podział ról (umowa projektu)

Utrzymanie strony i kodu: Claude Code (to repo). Treści, metodologia, decyzje: praca z autorem w Cowork. Wspólny styk to builder i pliki `.md` — dlatego zasada „wszystko przez builder" jest nienegocjowalna.

## Aktualizacja miesięczna

Kotwica: cykl 25. dnia miesiąca wg `INSTRUKCJA_aktualizacji.md`. Aktualizator dopisuje kotwice po ostatnim miesiącu z `talent_published.json`. `talent_daily.py` zapisuje tylko w `prototyp/data/research/`. Próby prospektywne TIP-0003 zapisują oddzielne pliki w `prototyp/data/prospektywny-test/`.
Od 2026-07-09 dzieje się automatycznie: GitHub Action `.github/workflows/publikacja_kotwicy.yml` (fetch_gus.py → talent_update.py → build_strona.py → commit) — ręczne uruchomienie/wyłączenie opisane w `INSTRUKCJA_aktualizacji.md` → „Automatyzacja".
Osobny GitHub Action, `.github/workflows/przebudowa_strony.yml`, przebudowuje stronę automatycznie po każdym pushu do `main`, który zmienia plik z `DOCS`, szablon albo builder — patrz `INSTRUKCJA_aktualizacji.md` → „Automatyzacja".
