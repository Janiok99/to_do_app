from todo import add_task, list_tasks, mark_done, delete_task, mark_undone

def main():
    while True:
        print("\n--- TO-DO MANAGER ---")
        print("1. Wyświetl zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz jako wykonane")
        print("4. Oznacz jako niewykonane")
        print("5. Usuń zadanie")
        print("6. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            list_tasks()

        elif choice == "2":
            title = input("Podaj treść zadania: ")
            add_task(title)

        elif choice == "3":
            index = int(input("Podaj numer zadania: ")) - 1
            mark_done(index)

        elif choice == "4":
            index = int(input("Podaj numer zadania: ")) - 1
            mark_undone(index)

        elif choice == "5":
            index = int(input("Podaj numer zadania: ")) - 1
            delete_task(index)

        elif choice == "6":
            print("Do zobaczenia!")
            break

        else:
            print("Nieprawidłowa opcja.")

if __name__ == "__main__":
    main()
