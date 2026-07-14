# Talent (TLN) — jednostka wartości minimalnego żalu

**Talent** to otwarta, deterministyczna jednostka rozliczeniowa do umów wieloletnich: pożyczasz 1000 TLN — oddajesz 1000 TLN, a obie strony odzyskują w przybliżeniu tę samą wartość. Formuła: **środek geometryczny indeksu cen i indeksu płac**, √(C×W). Matematycznie minimalizuje największą możliwą krzywdę którejkolwiek strony (kryterium minimax regret); empirycznie: najgorszy przypadek 6,1% przez sto lat danych USA (1929–2025) i 10,4% przez polską transformację ustrojową (1989–2024) — wobec setek procent dla pożyczek nominalnych.

Zasada projektu: **kod jest metodologią**. Wszystkie wartości są odtwarzalne z publicznych danych, publikowane z wyprzedzeniem i nigdy nie rewidowane wstecz.

## Zacznij tutaj

| Dokument | Co zawiera |
|---|---|
| [strona/whitepaper.md](strona/whitepaper.md) | **Whitepaper** — pełny wywód: problem, wzór z dowodem dla licealisty, testy, granice metody |
| [strona/wprowadzenie.md](strona/wprowadzenie.md) | Wprowadzenie — czym jest Talent i do czego służy |
| [strona/faq.md](strona/faq.md) | FAQ — krótkie, uczciwe odpowiedzi na typowe wątpliwości |
| [strona/regula_publikacyjna.md](strona/regula_publikacyjna.md) | Specyfikacja techniczna: definicje nóg, kalendarz publikacji, bezpieczniki |
| [TIP/](TIP/) | Talent Improvement Proposals — jawny proces zmian formuły (wzorzec BIP/EIP) |
| [talent_strona.html](talent_strona.html) | Strona z wartością bieżącą i wykresami (statyczna, działa z GitHub Pages) |

## Dowody empiryczne

- [materialy/wyscig_kandydatow.md](materialy/wyscig_kandydatow.md) — porównanie kandydatów na jednostkę (CPI, złoto, surowce, płace, mieszanki), 1996–2025
- [materialy/wyniki_test_stulecia_usa.md](materialy/wyniki_test_stulecia_usa.md) — USA 1929–2025: Wielki Kryzys, wojna, stagflacja, 2022
- [materialy/wyniki_kruche_gospodarki.md](materialy/wyniki_kruche_gospodarki.md) — Polska 1989–2024, Niemcy 1923, Argentyna (granice metody)
- [materialy/wyniki_talent_dwustronny.md](materialy/wyniki_talent_dwustronny.md) — jednostka umów międzynarodowych (PL-US)
- [materialy/ZRODLA_backtest_historyczny.md](materialy/ZRODLA_backtest_historyczny.md) — źródła danych do testów wstecznych

## Odtwórz obliczenia

```bash
cd prototyp
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # wpisz własny (darmowy) klucz API FRED
python src/talent_daily.py  # kotwice miesięczne + ścieżka dzienna
python src/regret_century.py  # test stulecia USA
python src/build_strona.py  # przebudowa strony
```

Dane wejściowe są w `prototyp/data/` (surowe pobrania + przetworzone wyniki), więc skrypty analiz działają bez pobierania.

## Struktura repozytorium

```
├── strona/                              # źródła MD artykułów witryny (nazwa md == nazwa html)
│   ├── whitepaper.md                    # whitepaper
│   ├── wprowadzenie.md                  # wprowadzenie
│   └── regula_publikacyjna.md           # specyfikacja
├── materialy/                           # strony dowodowe + dokumenty robocze (materiał pod podręcznik)
│   ├── wyniki_*.md, wyscig_*.md         # raporty z testów (kompilowane na stronę)
│   ├── ZRODLA_, SZKIC_, TALENTY_*.md    # zaplecze i szkice
│   └── waluty/                          # karty walutowe TALENT-XXX
├── TIP/                                 # proces zmian
├── *.html                               # strony publiczne (generowane przez builder)
├── prototyp/
│   ├── src/                             # aktywny kod (talent_daily, regret_*, build_strona)
│   └── data/                            # dane surowe i przetworzone
└── .github/workflows/                   # automatyzacja: miesięczna kotwica + przebudowa strony
```

## Skąd wziął się Talent

Talent nie powstał od razu. Wyrósł z szerszej, ambitniejszej próby — projektu **AUV (Absolute Unit of Value)**: zbudowania „absolutnej" miary wartości na koszyku surowców, produkcji i populacji. Krytyczna ocena ekonomiczna i testy na danych wykazały, że taka jednostka nie istnieje — a najcenniejszą częścią tamtej konstrukcji okazał się jej *mianownik* (dochód/praca), nie cały koszyk. Stąd zwrot: od „miary absolutnej" do wąskiej, weryfikowalnej **jednostki minimalnego żalu dla umów** — Talenta.

To repozytorium zawiera wyłącznie dojrzały wynik tej drogi. Pełna historia prób i błędów (AUV, FDI, AUV-T, recenzje, plany) jest zachowana osobno, w repozytorium-archiwum `globalny-wskaznik-wartosci`, wraz z dokumentem `PODSUMOWANIE_projektu.md` domykającym tamten etap. Zgodnie z filozofią projektu nie ukrywamy tej historii: błędy są częścią dowodu — po prostu nie muszą już zaśmiecać repozytorium o Talencie.

## Status

Prototyp badawczy. Znane prowizoria wymienione są jawnie w regule publikacyjnej (§7) i w artykule (§7 i §9). Dane płacowe GUS/ZUS dla Polski wymagają weryfikacji u źródła przed publikacją produkcyjną.

## Licencja

Kod i dokumentacja: [MIT](LICENSE) — używaj, kopiuj, modyfikuj bez ograniczeń. Jedna prośba (nie warunek prawny): jeśli zmieniasz formułę, nazwij wynik inaczej niż „Talent (TLN)" albo zaproponuj zmianę przez [TIP](TIP/) — żeby jedna nazwa zawsze oznaczała jedną, weryfikowalną definicję.
