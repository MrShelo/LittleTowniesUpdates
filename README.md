# Little Townies

Miejska gra budowlana 3D na siatce 64×64 (three.js). Waluta: T¢.

## Granie
Otwórz `index.html` w przeglądarce (potrzebny internet do wczytania three.js) albo użyj paczek Windows / Android.

## Aktualizacje w grze
W grze: Opcje → *Aktualizacje z GitHuba* → wpisz `użytkownik/little-townies` → *Sprawdź aktualizacje*.
Gra pobiera `version.json` i jeśli wersja jest nowsza, ściąga `index.html`, zapisuje go lokalnie i uruchamia. Zapis miasta zostaje.
Gdyby nowa wersja się nie uruchomiła, po 20 s gra sama wraca do wersji wbudowanej (albo: Opcje → *Wróć do wersji wbudowanej*).

## Wydawanie nowej wersji
1. Podbij `LT_VERSION` na początku `index.html` (np. `1.3.1`).
2. `python3 wydaj.py "krótki opis zmian"` – tworzy `version.json` i `update.js`.
3. `git add -A && git commit -m "v1.3.1" && git tag v1.3.1 && git push origin main --tags`

## Muzyka
Stacje radiowe: Nature FM, Luxury FM, Lofi Radio (`music/`).

## Edytor modeli
`edytor/LittleTownies-Edytor.html` – otwórz w przeglądarce (Edge/Chrome). Wczytuje grę z GitHuba, pozwala zmieniać części modeli
(kolor, położenie, obrót, skala, ukrycie) i dodawać bryły. Zapisane modele zostają na komputerze; zaznaczone można wysłać razem
jako jedną aktualizację (potrzebny token GitHuba z uprawnieniem *Contents: Read and write* do tego repozytorium).
Przy wydawaniu nowej wersji gry ręcznie użyj `python3 zachowaj_modele.py nowa.html` (po `git pull`), żeby nie skasować wysłanych modeli.
