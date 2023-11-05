import sqlite3
from datetime import datetime

class BazaDanych:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.connection = None
        self.cursor = None

    def bd_polacz(self):
        self.connection = sqlite3.connect(self.nazwa)
        self.cursor = self.connection.cursor()

    def bd_rozlacz(self):
        if self.connection:
            self.connection.close()

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

    def edytuj_dane(self, id, nowa_nazwa):
        self.bd_polacz()
        self.cursor.execute("UPDATE wydatki SET nazwa = ? WHERE id = ?", (nowa_nazwa, id))
        self.connection.commit()
        self.bd_rozlacz()

def main_menu():
	print("""Opcje:
[1] - Dodaj wydatek
[2] - Wyświetl wydatki
[3] - Edytuj wydatki
[4] - 
[5] -
[6] - Wyjście""")


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
    choice = int(input('Twój wybór: '))
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
    
def edytuj_wydatki():
    bazadanych = BazaDanych("wydatki.db")
    bazadanych.utworz_bd()
    
    edytuj_id = 1  # Identyfikator rekordu do edycji
    edytuj_nazwe = "ZaktualizowaneDane"
    bazadanych.edytuj_dane(edytuj_id, edytuj_nazwe)
    print(f"Zaktualizowano dane dla id {edytuj_id} na: {edytuj_nazwe}")
    
def zaktualizuj_wydatki():
    bazadanych = BazaDanych("wydatki.db")
    bazadanych.utworz_bd()
    
    zaktualizowane_dane = bazadanych.wyswietl_dane()
    print("Zaktualizowane dane:")
    for row in zaktualizowane_dane:
        print(row)
