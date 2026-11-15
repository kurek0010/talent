# Pochodzenie kotwic TLN-PLN od czerwca do września 2026 r.

**Data audytu:** 2026-11-15. Odtworzenie historycznych publikacji. Wartości w tabeli pozostają w dotychczasowej serii badawczej.

| Miesiąc | Commit publikacji i czas UTC | Uruchomienie i wersja kodu | CPI użyty (poprzedni miesiąc = 100) | Indeks płac | Kotwica odtworzona i zapisana |
|---|---|---|---:|---:|---:|
| 2026-06 | `bfc9eaf`, 25.07 10:21:12 | [30154294732](https://github.com/kurek0010/talent/actions/runs/30154294732), `3930d3c` | 99,7 (maj) | 909,026 | 582,329 |
| 2026-07 | `8c682ca`, 25.08 09:25:42 | [32831804647](https://github.com/kurek0010/talent/actions/runs/32831804647), `bfc9eaf` | 100,0 (domyślna wartość przy braku czerwca) | 913,307 | 583,698 |
| 2026-08 | `4f1cd51`, 25.09 14:18:37 | [36146528283](https://github.com/kurek0010/talent/actions/runs/36146528283), `8c682ca` | 100,0 (domyślna wartość przy braku lipca) | 913,307 | 583,698 |
| 2026-09 | `f11da70`, 25.10 13:27:35 | [40197620025](https://github.com/kurek0010/talent/actions/runs/40197620025), `4f1cd51` | 100,0 (domyślna wartość przy braku sierpnia) | 913,307 | 583,698 |

## Odtworzenie i przyczyna

Z każdego commita checkoutu wyeksportowano do odrębnego katalogu `talent_update.py`, `first_prints_pln.json`, CSV kotwic oraz rejestr publikacji. Uruchomiono sam historyczny aktualizator z datą danego uruchomienia. Odtworzenie można powtórzyć poleceniem `python prototyp/src/replay_kotwice_2026.py` z katalogu repozytorium. W każdym przypadku wynik był zgodny ze wszystkimi polami dopisanego wiersza CSV i z listą miesięcy w rejestrze. SHA-256 wspólnego pliku wejściowego to `53fb2dacf1eb8e3e5cd77be086bd8384d79f2d90c46f303374909d872ebc9b0d`. Logi lipcowej, sierpniowej i wrześniowej kotwicy potwierdzają brak nowych wejść, użycie 100,0 i wynik. Log uruchomienia 30154294732 wygasł (HTTP 410). Dla czerwca użycie 99,7 potwierdzają komunikat w commicie i zgodność rachunku. Wspólny rejestr zapisuje pobranie tego majowego CPI 9 lipca.

Dawny aktualizator zerował licznik braków przy każdym uruchomieniu, a przy braku odczytu dla ostatniej kotwicy podstawiał 100,0. Przy jednym nowym miesiącu w każdym uruchomieniu błąd się powtarzał i blokada drugiego kolejnego braku się nie uruchamiała. Commit `281350e` zmienił odnajdywanie CSV GUS i odtwarzanie ciągu braków między uruchomieniami. [Uruchomienie z 12 listopada](https://github.com/kurek0010/talent/actions/runs/43265001848) odczytało cztery brakujące dynamiki. Są widoczne w logu. Dotychczasowe kotwice już istniały, a workflow uzależniał zapis wejść do Git od nowej kotwicy lub nowych przeliczeń FX.

## Porównanie ze źródłami GUS

Doprecyzowanie z 2026-11-15. Wiersz lipcowy wskazuje 13 sierpnia jako dzień regularnej publikacji według kalendarza GUS. Ta korekta daty opisowej zachowuje wszystkie wartości i wnioski audytu. [Kalendarium GUS](https://stat.gov.pl/kalendarium/13-08-2026.html)

| Miesiąc | Regularny CPI m/m | Data publikacji |
|---|---:|---|
| Czerwiec | 99,5 | [GUS, 15.07.2026](https://publikacje.new.stat.gov.pl/portal-publikacje/wskazniki-cen-towarow-i-uslug-konsumpcyjnych-w-czerwcu-2026-r) |
| Lipiec | 100,8 | [GUS, 13.08.2026](https://publikacje.new.stat.gov.pl/portal-publikacje/wskazniki-cen-towarow-i-uslug-konsumpcyjnych-w-lipcu-2026-r) |
| Sierpień | 100,3 | [GUS, 15.09.2026](https://publikacje.new.stat.gov.pl/portal-publikacje/wskazniki-cen-towarow-i-uslug-konsumpcyjnych-w-sierpniu-2026-r) |
| Wrzesień | 100,7 | [GUS, 14.10.2026](https://stat.gov.pl/obszary-tematyczne/ceny-handel/wskazniki-cen/wskazniki-cen-towarow-i-uslug-konsumpcyjnych-we-wrzesniu-2026-r-%2C2%2C179.html) |

Każda regularna publikacja GUS poprzedzała nominalne odcięcie 24. dnia. Zgodność z logiem z 12 listopada potwierdza wartości w później pobranej tabeli. Nie zachowała się migawka tabeli użyta przez fetcher przy każdym z czterech historycznych uruchomień.

Dane roczne w rejestrze to potwierdzone 8 181,72 zł za 2024 r. i 8 903,56 zł za 2025 r. Wartość 9 419,96648 zł za 2026 r. jest zapisem proxy obliczonym jako 8 903,56 × 1,058. Projekt wykorzystał wzrost płac w sektorze przedsiębiorstw jako przybliżenie dynamiki płac rocznych w całej gospodarce. Do czerwca 2026 r. kod interpolował między lipcowymi punktami, lipiec osiągnął poziom proxy, a sierpień i wrzesień przeniosły ten sam poziom. [GUS, 2024 r.](https://stat.gov.pl/sygnalne/komunikaty-i-obwieszczenia/lista-komunikatow-i-obwieszczen/komunikat-w-sprawie-przecietnego-wynagrodzenia-w-gospodarce-narodowej-w-2024-r-%2C273%2C12.html) · [Monitor Polski, 2025 r.](https://eli.gov.pl/eli/MP/2026/192/ogl) · [GUS, sektor przedsiębiorstw, maj 2026](https://ssgk.stat.gov.pl/06.2026/Wynagrodzenia_i_swiadczenia_spoleczne.html)

Porównanie tablicy GUS z próbą `regret_poland.py` dało zgodność wszystkich 36 poziomów płac z lat 1989–2024, po przeliczeniu wartości sprzed 1995 r. przez 10 000. Przejście z 1 239,49 zł za 1998 r. do 1 706,74 zł za 1999 r. obejmuje zmianę definicji. Potwierdzenie nominalnych poziomów nie potwierdza przyjętego w badaniu łącznika 11,1% dla porównywalnej dynamiki. Próba pozostaje warunkowa do ustalenia porównywalnego odczytu. [GUS, wynagrodzenie 1950–2025](https://stat.gov.pl/obszary-tematyczne/rynek-pracy/pracujacy-zatrudnieni-wynagrodzenia-koszty-pracy/przecietne-miesieczne-wynagrodzenie-w-gospodarce-narodowej-w-latach-1950-2025%2C2%2C1.html)
