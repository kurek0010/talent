# TLN-PLN — karta polskiego prototypu

**Status:** prototyp badawczy dla polskiej gospodarki i rozliczeń w PLN. [Strona główna](../../index.html) · [Reguła publikacyjna](../../strona/regula_publikacyjna.md)

## Dane używane przez aktualizator

- **Ceny:** miesięczna dynamika CPI GUS z rejestru `first_prints_pln.json`.
- **Płace:** roczne przeciętne wynagrodzenia, interpolowane logarytmicznie między punktami lipcowymi. Po końcu interpolacji kod zachowuje ostatni poziom.

## Kandydaci do weryfikacji

HICP Polski ma wspólną bazę danych z CPI i może służyć do porównania metod. [Metadane HICP, §18.5.2](https://ec.europa.eu/eurostat/cache/metadata/EN/prc_hicp_esmshi4_pl.htm)

[TIP-0001](../../TIP/TIP-0001-noga-placowa-v02.md) opisuje badany wariant funduszu płac i wygładzonego zatrudnienia. [TIP-0002](../../TIP/TIP-0002-mediana-wynagrodzen.md) dotyczy mediany poziomów wynagrodzeń GUS. Dane nowego badania zaczynają się od stycznia 2024 r., a odczyt za marzec 2026 r. opublikowano 2 września 2026 r. [Zapowiedź GUS](https://stat.gov.pl/dla-mediow/informacje-prasowe/informacja-o-badaniu-rozklad-wynagrodzen-w-gospodarce-narodowej%2C2%2C1.html?contrast=default) · [Kalendarium GUS](https://stat.gov.pl/kalendarium/02-09-2026.html)

## Próba historyczna

Maksimum 10,4% w [próbie Polski 1989–2024](../wyniki_kruche_gospodarki.md) jest warunkowe na użytym szeregu płac i badanych horyzontach. Wszystkie poziomy potwierdzono w GUS po uwzględnieniu denominacji. Łączenie szeregów przy zmianie definicji płac w 1999 r. pozostaje przybliżeniem. [Audyt](../audyt_kotwic_2026.md)
