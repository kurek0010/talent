# TIP-0002 — mediana wynagrodzeń w gospodarce narodowej

**Autor:** Mariusz Kurowski · **Data:** 2026-07-07 · **Status:** Szkic

**Korekta 2026-11-15.** Poprawiono datę początku szeregu i opis opóźnienia. Doprecyzowano różnicę między medianą poziomów a medianą dynamik indywidualnych.

## Problem

Aktualizator używa interpolowanych rocznych przeciętnych wynagrodzeń. W badaniu alternatywnych miar warto ocenić wrażliwość na zmiany składu populacji i na skrajne obserwacje. Wyższy poziom średniej od mediany sam w sobie nie wskazuje, która miara rośnie szybciej.

## Kandydat

Mediana miesięcznych wynagrodzeń brutto z badania GUS „Rozkład wynagrodzeń w gospodarce narodowej” opartego na źródłach administracyjnych. Pierwsze dane dotyczą stycznia 2024 r. i ukazały się we wrześniu 2024 r. Dane za marzec 2026 r. opublikowano 2 września 2026 r., około pięciu miesięcy po końcu badanego miesiąca. Potrzebna jest analiza rzeczywistych dat dostępności. [Zapowiedź GUS](https://stat.gov.pl/dla-mediow/informacje-prasowe/informacja-o-badaniu-rozklad-wynagrodzen-w-gospodarce-narodowej%2C2%2C1.html?contrast=default) · [Kalendarium GUS](https://stat.gov.pl/kalendarium/02-09-2026.html)

Zmiana mediany poziomów wynagrodzeń może odzwierciedlać zmianę składu badanej populacji. Mediana indywidualnych zmian wynagrodzenia tych samych osób wymaga odrębnych danych i definicji. Aktualizator nie korzysta z żadnej z tych miar.

## Testy przed decyzją

1. Porównać dynamiki na wspólnym odcinku szeregu, począwszy od 2024 r., z uwzględnieniem różnic w populacji i definicjach.
2. Zbadać rewizje i opóźnienia oraz zasymulować dostępność danych w dniu publikacji.
3. Ocenić, czy krótki szereg wystarcza do wniosków o skutkach dla obu stron. Przed przyjęciem wariantu ustalić kryteria porównania oraz zasady postępowania w okresach braku odczytu.
