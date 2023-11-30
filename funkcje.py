from class_BazaDanych import BazaDanych
from datetime import datetime
from dane_uzytkowe import *
def wybor_daty():
    while True:
        data_str = input("Podaj datę w formacie DD-MM-RRRR: ")
        try:
            data = datetime.strptime(data_str, "%d-%m-%Y")
            data = data.date()
            # print(f"Wybrana data: {data}")
            return data  # Wyjście z pętli, gdy data jest poprawna
        except ValueError:
            print("Błędny format daty. Spróbuj ponownie.")

def wybor_kategori():
    print("""Wybierz kategorie zakupów:
[1] - wydatki podstawowe
[2] - dom i rachunki
[3] - rozrywka i podróże
[4] - zdrowie i uroda
[5] - odzież i obuwie
[6] - pozostałe""")

    while True:
        try:
            choice = int(input('Twój wybór: '))
            break
        except ValueError:
            print('Wybrano błędną wartość. Wybierz ponownie. ')
            continue

    if choice == 1:
        kategoria = 'wydatki podstawowe'
    elif choice == 2:
        kategoria = 'dom i rachunki'
    elif choice == 3:
        kategoria = 'rozrywka i podróże'
    elif choice == 4:
        kategoria = 'zdrowie i uroda'
    elif choice == 5:
        kategoria = 'odzież i obuwie'
    else:
        kategoria = 'pozostałe'
    return kategoria

def pokaz_wydatki():
    bazadanych = BazaDanych("wydatki.db")
    bazadanych.utworz_bd()

    aktualne_dane = bazadanych.wyswietl_dane()
    print("Aktualne wydatki:")
    for row in aktualne_dane:
        print(row)

def dodaj_wydatek():
    bazadanych = BazaDanych("wydatki.db")
    bazadanych.utworz_bd()

    nazwa_wydatku = input("Podaj nazwe paragonu(sklep): ")
    kwota = input("Podaj kwote paragonu: ")
    kwota = kwota.replace(',', '.')
    kwota = float(kwota)
    data = wybor_daty()
    kategoria = wybor_kategori()
    bazadanych.dodaj_dane(nazwa_wydatku, kwota, data, kategoria)
    print(f"Dodano nowe dane: {nazwa_wydatku},{kwota},{data},{kategoria}")

def wybor_id_do_edycji():
    edytuj_id = None
    while True:
        try:
            edytuj_id = int(input('Wybierz id wydatku do edycji: '))  # Identyfikator rekordu do edycji
            return edytuj_id
        except ValueError:
            print('Wybrano błędną wartość. Wybierz ponownie. ')
            continue

def menu_edycji_danych():
    choice = None
    print("""Jakie dane chcesz zmienic? 
    [1] - nazwa
    [2] - kwota
    [3] - data
    [4] - kategoria
    [5] - powrót""")

    while True:
        try:
            choice = int(input('Twój wybór: '))
            return choice
        except ValueError:
            print('Wybrano błędną wartość. Wybierz ponownie. ')
            continue

def edytuj_wydatki():
    bazadanych = BazaDanych("wydatki.db")
    bazadanych.utworz_bd()

    edytuj_id = wybor_id_do_edycji()

    choice = menu_edycji_danych()

    if choice == 1:
        nowa_nazwa = input('Podaj nową nazwe: ')
        bazadanych.update_nazwa(edytuj_id, nowa_nazwa)
        print(f"Zaktualizowano dane dla id {edytuj_id} na: {nowa_nazwa}")

    elif choice == 2:
        nowa_kwota = input('Podaj nową kwote: ')
        nowa_kwota = nowa_kwota.replace(',', '.')
        nowa_kwota = float(nowa_kwota)
        bazadanych.update_kwota(edytuj_id, nowa_kwota)
        print(f"Zaktualizowano dane dla id {edytuj_id} na: {nowa_kwota}")

    elif choice == 3:
        while True:
            nowa_data_str = input('Podaj nową date w formacie DD-MM-RRR: ')
            try:
                nowa_data = datetime.strptime(nowa_data_str, "%d-%m-%Y")
                nowa_data = nowa_data.date()
                break
            except ValueError:
                print("Błędny format daty. Spróbuj ponownie.")

        bazadanych.update_data(edytuj_id, nowa_data)
        print(f"Zaktualizowano dane dla id {edytuj_id} na: {nowa_data}")

    elif choice == 4:
        print("""Wybierz na którą kategorię zakupów chcesz zmienić:
[1] - wydatki podstawowe
[2] - dom i rachunki
[3] - rozrywka i podróże
[4] - zdrowie i uroda
[5] - odzież i obuwie
[6] - pozostałe""")
        while True:
            try:
                choice_2 = int(input('Twój wybór: '))
                break
            except ValueError:
                print('Wybrano błędną wartość. Wybierz ponownie. ')
                continue
        if choice_2 == 1:
            nowa_kategoria = 'wydatki podstawowe'
        elif choice_2 == 2:
            nowa_kategoria = 'dom i rachunki'
        elif choice_2 == 3:
            nowa_kategoria = 'rozrywka i podróże'
        elif choice_2 == 4:
            nowa_kategoria = 'zdrowie i uroda'
        elif choice_2 == 5:
            nowa_kategoria = 'odzież i obuwie'
        else:
            nowa_kategoria = 'pozostałe'

        bazadanych.update_kategoria(edytuj_id, nowa_kategoria)
        print(f"Zaktualizowano dane dla id {edytuj_id} na: {nowa_kategoria}")

    elif choice == 5:
        return
    else:
        print("Wybierz ponownie. ")

def sortuj_wg_zakresu_dat_menu():
    bazadanych = BazaDanych("wydatki.db")
    bazadanych.utworz_bd()

    print("Podaj date początkową")
    data_poczatkowa = wybor_daty()
    print("Podaj date końcową")
    data_koncowa = wybor_daty()

    sortowane_dane = bazadanych.sortuj_wg_zakresu_dat(data_poczatkowa, data_koncowa)

    print(f"Paragony z okresu od {data_poczatkowa} do {data_koncowa}:")
    for row in sortowane_dane:
        print(row)

def sortuj_wg_miesiaca_menu():
    bazadanych = BazaDanych("wydatki.db")
    bazadanych.utworz_bd()
    while True:
        try:
            rok = input("Podaj rok w formacie RRRR: ")
            if len(rok) != 4:
                print("Błąd")
                continue
            else:
                rok = int(rok)
            break
        except ValueError:
            print('Wybrano błędną wartość. Wybierz ponownie. ')
            continue

    while True:
        try:
            miesiac = input("Podaj miesiac w formacie MM:")
            if len(miesiac) != 2:
                print("Błąd")
                continue
            else:
                miesiac = int(miesiac)
            break
        except ValueError:
            print('Wybrano błędną wartość. Wybierz ponownie. ')
            continue

    sortowane_dane = bazadanych.sortuj_wg_miesiaca(rok, miesiac)

    for row in sortowane_dane:
        print(row)

def suma_z_zakresu_menu():
    bazadanych = BazaDanych("wydatki.db")
    bazadanych.utworz_bd()

    print("Podaj date początkową")
    data_poczatkowa = wybor_daty()
    print("Podaj date końcową")
    data_koncowa = wybor_daty()

    suma = bazadanych.suma_z_zakresu(data_poczatkowa, data_koncowa)
    print(f"Wydana kwota z okresu od {data_poczatkowa} do {data_koncowa} to: {suma}zł")

def suma_z_miesiaca_menu():
    bazadanych = BazaDanych("wydatki.db")
    bazadanych.utworz_bd()
    while True:
        try:
            rok = input("Podaj rok w formacie RRRR: ")
            if len(rok) != 4:
                print("Błąd")
                continue
            else:
                rok = int(rok)
            break
        except ValueError:
            print('Wybrano błędną wartość. Wybierz ponownie. ')
            continue

    while True:
        try:
            miesiac = input("Podaj miesiac w formacie MM:")
            if len(miesiac) != 2:
                print("Błąd")
                continue
            else:
                miesiac = int(miesiac)
            break
        except ValueError:
            print('Wybrano błędną wartość. Wybierz ponownie. ')
            continue

    suma = bazadanych.suma_z_miesiaca(rok, miesiac)
    nazwa_miesiaca = get_nazwa_miesiaca(miesiac)

    print(f"Wydana kwota z miesiąca {nazwa_miesiaca} to: {suma}zł")