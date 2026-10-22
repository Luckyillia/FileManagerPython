import datetime
from pathlib import Path

DANE = Path('dane.txt')
programExit = False
now = datetime.datetime.now()

def wyswietl_dane(arr, isNumeric):
        for numer, user in enumerate(arr, start=1):
            if(isNumeric):
                print(f"{numer}. {user.strip()}")
            else:
                print(f"{user.strip()}")

def wczytaj_dane(PLIK, arr):
    with open(PLIK, "r", encoding="utf-8") as f:
        for user in f:
            arr.append(user.strip())

def zapisz_dane(PLIK, arr):
    try:
        with open(PLIK, "w", encoding="utf-8") as f:
            for user in arr:
                f.write(str(user).strip() + "\n")
    except (OSError, IOError) as e:
        print(f"Błąd zapisu do PLIKu '{PLIK}': {e}")

def delete_record(PLIK, arr, index):
    try:
        with open(PLIK, "w", encoding="utf-8") as f:
            for numer, user in enumerate(arr, start=1):
                if numer != index:
                    f.write(str(user).strip() + "\n")
    except (OSError, IOError) as e:
        print(f"Błąd zapisu do PLIKu '{PLIK}': {e}")

def add_data(PLIK, arr, data):
    arr.append(data)
    zapisz_dane(PLIK, arr)
    print("Dane zostaly dodane\n")

def rewrite_file(PLIK, arr, data):
    arr = []
    arr.append(data)
    zapisz_dane(PLIK, arr)
    print("Dane zostaly nadpisane\n")

def clean_file(PLIK, arr):
    arr = []
    try:
        with open(PLIK, "w", encoding="utf-8") as f:
            pass
        print("Dane zostaly wyczyszczone\n")
    except (OSError, IOError) as e:
        print(f"Błąd zapisu do PLIKu '{PLIK}': {e}")

def search_text(word, arr):
    count = 0
    word = word.lower()
    for line in arr:
        if word in line.lower():
            count += 1
    return count

while programExit == False:
    if not DANE.exists():
        print("Nie znaleziono tab.txt, plik byl utworzony automatycznie")
        with open(DANE, "w", encoding="utf-8") as f:
            pass
    print("\n1. Wyswietl dane pliku\n2. Dodaj dane do pliku\n3. Nadpisz plik\n4. Wyczyszc plik\n5. Wyszukaj\n6. Wyswietl numerowano\n7. Zakoncz program\n")
    opcja = int(input("Wybierz opcje(1,2,3,4,5,6,7): "))
    tab = []
    wczytaj_dane(DANE, tab)
    if opcja == 1:
        wyswietl_dane(tab, False)
    elif opcja == 2:
        dane = input("Napisz co chcesz dodac: ")
        add_data(DANE, tab, dane)
    elif opcja == 3:
        dane = input("Napisz tekst: ")
        rewrite_file(DANE, tab, dane)
    elif opcja == 4:
        clean_file(DANE, tab)
    elif opcja == 5:
        wordPhrase = input("Napisz co chcesz wyszukac: ")
        print(f"Slowo {wordPhrase} wystepuje w pliku {search_text(wordPhrase, tab)}")
    elif opcja == 6:
        wyswietl_dane(tab, True)
    elif opcja == 7:
        programExit = True
    else:
        print("Nie znana opcja")