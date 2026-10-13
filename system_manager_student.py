import datetime
from pathlib import Path

DANE = Path('uczniowie.txt')
programExit = False
now = datetime.datetime.now()

def wyswietl_dane(arr):
        for numer, user in enumerate(arr, start=1):
            print(f"{numer}. {user.strip()}")

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


while programExit == False:
    if not DANE.exists():
        print("Nie znaleziono uczniowie.txt, plik byl utworzony automatycznie")
        with open(DANE, "w", encoding="utf-8") as f:
            pass
    print("\n1. Wyswietl liste uczniow\n2. Posortuj liste alfabetycznie\n3. Usun ucznia z listy\n4. Zakoncz program\n")
    opcja = int(input("Wybierz opcje(1,2,3,4): "))
    uczniowie = []
    wczytaj_dane(DANE, uczniowie)
    if opcja == 1:
        wyswietl_dane(uczniowie)
    elif opcja == 2:
        tab = []
        PLIK = Path(now.strftime("%Y-%m-%d-%H-%M-%S") + ".txt")
        wczytaj_dane(DANE,tab)
        tab.sort()
        zapisz_dane(PLIK, tab)
        wyswietl_dane(tab)
    elif opcja == 3:
        wyswietl_dane(uczniowie)
        index = int(input("Wybirz ucznia z listy: "))
        delete_record(DANE, uczniowie, index)
        uczniowie = []
        wczytaj_dane(DANE, uczniowie)
        wyswietl_dane(uczniowie)
    elif opcja == 4:
        programExit = True
    else:
        print("Nie znana opcja")