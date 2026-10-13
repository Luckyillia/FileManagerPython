import datetime
from pathlib import Path

DANE = Path('dane_tekstowe_do_sortowania.txt')
programExit = False
now = datetime.datetime.now()

def wyswietl_dane(PLIK):
    with open(PLIK, "r", encoding="utf-8") as f:
        for numer, user in enumerate(f, start=1):
            print(f"{numer}. {user.strip()}")

def wczytaj_dane(PLIK, arr):
    with open(PLIK, "r", encoding="utf-8") as f:
        for user in f:
            arr.append(user.strip())
def zapisz_dane(PLIK, arr):
    with open(PLIK, "r", encoding="utf-8") as f:
        for user in tab:
            f.write(user.strip())

while programExit == False:
    print("1. Wyswietl dane\n2. Posortuj dane\n3.Zakoncz program\n")
    opcja = int(input("Wybierz opcje(1,2,3): "))
    if opcja == 1:
        wyswietl_dane(DANE)
    elif opcja == 2:
        tab = []
        PLIK = Path(now.strftime("%Y-%m-%d-%H-%M-%S") + ".txt")
        wczytaj_dane(DANE,tab)
        tab.sort()
        zapisz_dane(PLIK, tab)
        wyswietl_dane(PLIK)
    elif opcja == 3:
        programExit = True