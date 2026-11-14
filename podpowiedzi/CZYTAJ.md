# Podpowiedzi (teksty po najechaniu)

Tu edytujesz teksty, które gra pokazuje po najechaniu na przycisk albo narzędzie, razem z tłumaczeniami.

**Plik:** `podpowiedzi.xlsx` – zwykły plik Excela (działa też w LibreOffice i Google Sheets). Arkusz „Podpowiedzi”:

| kolumna | co to |
|---|---|
| klucz | nie zmieniaj – mówi grze, gdzie wstawić tekst (`el.…` = przycisk/kafelek, `tool.…` = narzędzie lub budynek) |
| gdzie | opis dla Ciebie, gra go nie używa |
| PL | tekst po polsku |
| EN | tłumaczenie angielskie (puste = zostaje polski) |
| DE | tłumaczenie niemieckie (puste = zostaje polski) |

Po zmianie PL popraw też EN i DE – tłumaczenie z tego pliku ma pierwszeństwo przed wbudowanym słownikiem.
Usunięty wiersz = gra użyje swojego wbudowanego tekstu.

**Jak to trafia do gry:** zapisz plik normalnie (ta sama nazwa, format .xlsx) i wypchnij na GitHub – przy każdym wydaniu wersji jest wstawiany do `index.html` automatycznie.
Żeby sprawdzić od razu u siebie: `python3 podpowiedzi/wstaw.py index.html` (bez dodatkowych bibliotek), potem otwórz `index.html`.
