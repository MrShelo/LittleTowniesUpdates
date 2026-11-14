# Podpowiedzi (teksty po najechaniu)

Tu edytujesz teksty, które gra pokazuje po najechaniu na przycisk albo narzędzie, razem z tłumaczeniami.

**Plik:** `podpowiedzi.tsv` – otwórz w Excelu, LibreOffice, Google Sheets albo zwykłym edytorze (kolumny rozdziela tabulator).

| kolumna | co to |
|---|---|
| klucz | nie zmieniaj – mówi grze, gdzie wstawić tekst (`el.…` = przycisk/kafelek, `tool.…` = narzędzie lub budynek) |
| gdzie | opis dla Ciebie, gra go nie używa |
| PL | tekst po polsku |
| EN | tłumaczenie angielskie (puste = zostaje polski) |
| DE | tłumaczenie niemieckie (puste = zostaje polski) |

Po zmianie PL popraw też EN i DE – tłumaczenie z tego pliku ma pierwszeństwo przed wbudowanym słownikiem.

**Jak to trafia do gry:** przy każdym wydaniu wersji plik jest wstawiany do `index.html` automatycznie.
Żeby sprawdzić od razu u siebie: `python3 podpowiedzi/wstaw.py index.html`, potem otwórz `index.html`.

Zapisując w Excelu wybierz „Tekst (rozdzielany znakami tabulacji)” i kodowanie UTF-8.
