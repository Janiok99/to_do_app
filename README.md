# To‑Do Manager
    Prosta aplikacja konsolowa do zarządzania zadaniami. Umożliwia dodawanie, usuwanie i oznaczanie zadań jako wykonane lub niewykonane, a wszystkie dane zapisuje w pliku tasks.json.

## Funkcjonalności
    - Dodawanie nowych zadań
    - Wyświetlanie listy zadań
    - Oznaczanie zadań jako wykonane
    - Oznaczanie zadania jako niewykonane 
    - Usuwanie zadań
    - Automatyczny zapis do pliku tasks.json
    - Brak zewnętrznych zależności — działa na czystym Pythonie

## Struktura projektu
todo-app/
│
├── src/
│     ├── storage.py      # obsługa pliku JSON
│     ├── todo.py         # logika aplikacji
│     └── main.py         # menu i interakcja z użytkownikiem
│
├── tasks.json            # plik z zadaniami (tworzy się automatycznie)
│
└── README.md

## Jak uruchomić projekt
    1.Przejdź do folderu projektu: 
        cd todo-app
    2. Uruchom aplikację:
        python src/main.py
    3. Korzystaj z menu w terminalu:
        --- TO-DO MANAGER ---
        1. Wyświetl zadania
        2. Dodaj zadanie
        3. Oznacz jako wykonane
        4. Oznacz jako niewykonane
        5. Usuń zadanie
        6. Wyjście

## Wymagania
    Projekt nie wymaga żadnych dodatkowych bibliotek.
    Działa na standardowej instalacji Python 3.8+.

## Jak działa zapis danych?
    Aplikacja przechowuje zadania w pliku tasks.json w formacie:
        [
            {
                "title": "Stworzyć repozytorium na Github",
                "done": false
            }
        ]   
    Plik tworzy się automatycznie przy pierwszym dodaniu zadania.

