# Talent (TLN) — propozycja standardu rozliczania umów

Talent to propozycja wspólnego standardu rozliczania umów dla osób prywatnych i przedsiębiorstw. W rozwijanej obecnie polskiej wersji opiera się na otwartej regule waloryzacji, która według uzgodnionej wcześniej zasady dzieli między strony wpływ zmian cen i przeciętnych wynagrodzeń. Strony przyjmują tę regułę dobrowolnie. Obecny zakres to polska gospodarka i rozliczenia w PLN.

Jawność reguły, danych i obliczeń ma umożliwiać niezależne odtworzenie wyniku oraz ocenę skutków przyjętej zasady. Projekt pozostaje prototypem badawczym. Jego zastosowania i ograniczenia są przedmiotem weryfikacji.

## Dokumentacja

- [Wprowadzenie](strona/wprowadzenie.md) i [FAQ](strona/faq.md) omawiają zasadę waloryzacji na przykładach pożyczki i płatności odroczonej.
- [Whitepaper](strona/whitepaper.md) definiuje indeks jako średnią geometryczną cen i płac. Dowód minimalizacji dotyczy konkretnej dwustronnej miary żalu w modelu jednej płatności.
- [Reguła publikacyjna](strona/regula_publikacyjna.md) i [polityka danych](POLITYKA_danych_v0.1.md) opisują miesięczną aktualizację i ograniczenia prototypu. Zmiany metody przechodzą przez [TIP](TIP/).
- [Kalkulator waloryzacji umowy](index.html#waloryzacja) porównuje płatność nominalną, CPI i Talent na historycznych odczytach miesięcznych. [Przelicznik walutowy](index.html#dane) pokazuje odpowiedniki polskiej kotwicy.

## Wyniki historyczne

- [Polska 1989–2024](materialy/wyniki_kruche_gospodarki.md). Maksimum żalu w badanych oknach wynosi 10,4%. Poziomy płac są zgodne z tablicą GUS, a łącznik przy zmianie definicji w 1999 r. pozostaje przybliżeniem. Epizody zagraniczne opisano jako materiał porównawczy.
- [USA](materialy/wyniki_test_stulecia_usa.md). W badanych horyzontach 3, 5, 10, 20 i 30 lat maksimum wynosi 6,1% dla CPI i płac (1939–2025) oraz 19,7% dla CPI i PKB na osobę (1929–2025).
- [Eksperyment PL–US](materialy/wyniki_talent_dwustronny.md) i [karty zagraniczne](materialy/waluty/) dokumentują dalsze tematy badawcze.
- [Porównanie kandydatów](materialy/wyscig_kandydatow.md) i [źródła historycznego testu AUV](materialy/ZRODLA_backtest_historyczny.md) są archiwalne i mają ograniczoną odtwarzalność. AUV (Absolute Unit of Value) był wcześniejszym projektem opartym m.in. na koszyku surowców.

W [walidacji polskich umów](materialy/walidacja_talent_pl.md) porównano cztery reguły dla rat i płatności odroczonej, z analizą płynności oraz kontrolą czterech historycznych publikacji. Dalsza walidacja odczytów na dzień publikacji wymaga archiwum cykli TIP-0003.

## Przebudowa strony i odtwarzanie badań

```bash
cd prototyp
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/build_strona.py
```

Builder korzysta z zapisanych danych. Skrypt dzienny zapisuje demonstrację w `prototyp/data/research/`. Odrębna reguła prospektywna jest w testach [TIP-0003](TIP/TIP-0003-tln-pln-prospektywny.md). [Dokumentacja prototypu](prototyp/README.md)

## Licencja

Kod i dokumentacja: [MIT](LICENSE) — używaj, kopiuj, modyfikuj bez ograniczeń. Jedna prośba (nie warunek prawny): jeśli zmieniasz formułę, nazwij wynik inaczej niż „Talent (TLN)" albo zaproponuj zmianę przez [TIP](TIP/) — żeby jedna nazwa zawsze oznaczała jedną, weryfikowalną definicję.
