import sqlite3
from datetime import datetime
from App_zaliczenie.dane_uzytkowe import *
class BazaDanych:
    def __init__(self, nazwa):
        self.nazwa = nazwa #Kod > BazaDanych("wydatki.db") w nawiasie ma nazwe do ktorej odnosza sie operacje wykonywane na bazie danych
        self.connection = None
        self.cursor = None
    def bd_polacz(self):
        self.connection = sqlite3.connect(self.nazwa) #Po wykonaniu tej linii kodu self.connection staje się obiektem reprezentującym połączenie z bazą danych o nazwie podanej w init jako nazwa
        self.cursor = self.connection.cursor() #a linia tworzy kursor, który jest używany do wykonywania operacji na bazie danych. Kursor jest powiązany z danym połączeniem, co oznacza, że operacje wykonywane za pomocą tego kursora będą miały wpływ na tę konkretną bazę danych.
        #Ogólnie rzecz biorąc, te linie kodu inicjują połączenie z bazą danych SQLite i tworzą kursor, który będzie używany do wykonywania zapytań i operacji na tej bazie danych.
    def bd_rozlacz(self):
        if self.connection is not None:  #To jest instrukcja warunkowa (warunek if), która sprawdza, czy atrybut self.connection (który jest obiektem reprezentującym połączenie z bazą danych) istnieje i nie jest równy None
            self.connection.close() #zamyka polaczenie
    def utworz_bd(self):
        self.bd_polacz()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS wydatki (
	        id INTEGER PRIMARY KEY,
	        nazwa TEXT,
	        kwota REAL,
	        data DATE,
	        kategoria TEXT)''')
        self.connection.commit()
        self.bd_rozlacz()
    def wyswietl_dane(self):
        self.bd_polacz()
        self.cursor.execute("SELECT * FROM wydatki")
        rows = self.cursor.fetchall()
        self.bd_rozlacz()
        return rows
    def dodaj_dane(self, nazwa,kwota,data,katgoria):
        self.bd_polacz()
        self.cursor.execute("INSERT INTO wydatki (nazwa,kwota,data,kategoria) VALUES (?,?,?,?)", (nazwa,kwota,data,katgoria))
        self.connection.commit()
        self.bd_rozlacz()
    def update_nazwa(self, id, nowa_nazwa):
        self.bd_polacz()
        self.cursor.execute("UPDATE wydatki SET nazwa = ? WHERE id = ?", (nowa_nazwa, id))
        self.connection.commit()
        self.bd_rozlacz()
    def update_kwota(self, id, nowa_kwota):
        self.bd_polacz()
        self.cursor.execute("UPDATE wydatki SET kwota = ? WHERE id = ?", (nowa_kwota, id))
        self.connection.commit()
        self.bd_rozlacz()
    def update_data(self, id, nowa_data):
        self.bd_polacz()
        self.cursor.execute("UPDATE wydatki SET data = ? WHERE id = ?", (nowa_data, id))
        self.connection.commit()
        self.bd_rozlacz()
    def update_kategoria(self, id, nowa_kategoria):
        self.bd_polacz()
        self.cursor.execute("UPDATE wydatki SET kategoria = ? WHERE id = ?", (nowa_kategoria, id))
        self.connection.commit()
        self.bd_rozlacz()
    def sortuj_wg_zakresu_dat(self, data_poczatkowa,data_koncowa):
        self.bd_polacz()
        self.cursor.execute("""SELECT * FROM wydatki WHERE data BETWEEN ? AND ? ORDER BY data """,
                            (data_poczatkowa,data_koncowa))
        rows = self.cursor.fetchall()
        self.bd_rozlacz()
        return rows
    def sortuj_wg_miesiaca(self, rok, miesiac):
        self.bd_polacz()
        pierwszy_dzien_miesiaca = f'{rok:04d}-{miesiac:02d}-01'
        ostatni_dzien_miesiaca = f'{rok:04d}-{miesiac:02d}-32'  # tworze str w formacie RRRR-MM-DD
        self.cursor.execute("SELECT * FROM wydatki WHERE data BETWEEN ? AND ? ORDER BY data",
                            (pierwszy_dzien_miesiaca, ostatni_dzien_miesiaca)) #zmienne wskakuja w miejsce znakow ?
        rows = self.cursor.fetchall()
        self.bd_rozlacz()
        return rows
    def suma_z_zakresu(self, data_poczatkowa, data_koncowa):
        self.bd_polacz()
        self.cursor.execute("SELECT SUM(kwota) FROM wydatki WHERE data BETWEEN ? AND ?",
                            (data_poczatkowa, data_koncowa))
        suma = self.cursor.fetchone()[0]  # Pobierz wynik sumy z kursora
        self.bd_rozlacz()
        return suma if suma is not None else 0
    def suma_z_miesiaca(self, rok, miesiac):
        self.bd_polacz()
        pierwszy_dzien_miesiaca = f'{rok:04d}-{miesiac:02d}-01'
        ostatni_dzien_miesiaca = f'{rok:04d}-{miesiac:02d}-32'  # tworze str w formacie RRRR-MM-DD
        self.cursor.execute("SELECT SUM(kwota) FROM wydatki WHERE data BETWEEN ? AND ?",
                            (pierwszy_dzien_miesiaca, ostatni_dzien_miesiaca))
        suma = self.cursor.fetchone()[0]
        self.bd_rozlacz()
        return suma if suma is not None else 0

def wybor_daty():
    while True:
        data_str = input("Podaj datę w formacie DD-MM-RRRR: ")
        try:
            data = datetime.strptime(data_str, "%d-%m-%Y")
            data = data.date()
            #print(f"Wybrana data: {data}")
            return data # Wyjście z pętli, gdy data jest poprawna
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
    kwota = kwota.replace(',','.')
    kwota = float(kwota)
    data = wybor_daty()
    kategoria = wybor_kategori()
    bazadanych.dodaj_dane(nazwa_wydatku,kwota,data,kategoria)
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
        bazadanych.update_nazwa(edytuj_id,nowa_nazwa)
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

    sortowane_dane = bazadanych.sortuj_wg_miesiaca(rok,miesiac)

    for row in sortowane_dane:
        print(row)
def suma_z_zakresu_menu():
    bazadanych = BazaDanych("wydatki.db")
    bazadanych.utworz_bd()

    print("Podaj date początkową")
    data_poczatkowa = wybor_daty()
    print("Podaj date końcową")
    data_koncowa = wybor_daty()

    suma = bazadanych.suma_z_zakresu(data_poczatkowa,data_koncowa)
    print(f"Wydana kwota z okresu od {data_poczatkowa} do {data_koncowa} to: {suma}zł")
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

    suma = bazadanych.suma_z_miesiaca(rok, miesiac)
    nazwa_miesiaca = get_nazwa_miesiaca(miesiac)

    print(f"Wydana kwota z miesiąca {nazwa_miesiaca} to: {suma}zł")