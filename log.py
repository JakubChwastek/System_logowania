
def znajdz_usera(nazwa, haslo):
    with open("users.txt", "r") as file:
        i=0
        lines = file.readlines()
        for line in lines:
            if nazwa in line and haslo in line:
                print(f"Witaj {nazwa}")
                i=1
        if i==0: nowy_user()

        file.close()

def podaj_dane():
    nazwa = input("Podaj nazwę użytkownika: \n")
    haslo = input("Podaj haslo: \n")
    znajdz_usera(nazwa, haslo)

def nowy_user():
    print("Nie ma takiego użytkownika w bazie! Czy chcesz stworzyc nowego uzytkownika? [Y/N]")
    value = input()
    f = open("users.txt", "a")
    if value == "Y":
        nazwa = input("Podaj nazwę użytkownika: \n")
        haslo = input("Podaj haslo: \n")
        mail = input("Podaj email: \n")
        f.write(f"\n{nazwa} ")
        f.write(f"{haslo} ")
        f.write(f"{mail} ")

    else: print("Dziękuję, do widzenia!")

    f.close()

podaj_dane()