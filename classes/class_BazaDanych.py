import sqlite3
from datetime import datetime
from dane_uzytkowe import *


class BazaDanych:
    def __init__(self, nazwa):
        self.nazwa = nazwa  # Kod > BazaDanych("wydatki.db") w nawiasie ma nazwe do ktorej odnosza sie operacje wykonywane na bazie danych
        self.connection = None
        self.cursor = None

    def bd_polacz(self):
        self.connection = sqlite3.connect(
            self.nazwa)  # Po wykonaniu tej linii kodu self.connection staje się obiektem reprezentującym połączenie z bazą danych o nazwie podanej w init jako nazwa
        self.cursor = self.connection.cursor()  # a linia tworzy kursor, który jest używany do wykonywania operacji na bazie danych. Kursor jest powiązany z danym połączeniem, co oznacza, że operacje wykonywane za pomocą tego kursora będą miały wpływ na tę konkretną bazę danych.
        # Ogólnie rzecz biorąc, te linie kodu inicjują połączenie z bazą danych SQLite i tworzą kursor, który będzie używany do wykonywania zapytań i operacji na tej bazie danych.

    def bd_rozlacz(self):
        if self.connection is not None:  # To jest instrukcja warunkowa (warunek if), która sprawdza, czy atrybut self.connection (który jest obiektem reprezentującym połączenie z bazą danych) istnieje i nie jest równy None
            self.connection.close()  # zamyka polaczenie

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

    def dodaj_dane(self, nazwa, kwota, data, kategoria):
        self.bd_polacz()
        self.cursor.execute("INSERT INTO wydatki (nazwa,kwota,data,kategoria) VALUES (?,?,?,?)",
                            (nazwa, kwota, data, kategoria))
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

    def sortuj_wg_zakresu_dat(self, data_poczatkowa, data_koncowa):
        self.bd_polacz()
        self.cursor.execute("""SELECT * FROM wydatki WHERE data BETWEEN ? AND ? ORDER BY data """,
                            (data_poczatkowa, data_koncowa))
        rows = self.cursor.fetchall()
        self.bd_rozlacz()
        return rows

    def sortuj_wg_miesiaca(self, rok, miesiac):
        self.bd_polacz()
        pierwszy_dzien_miesiaca = f'{rok:04d}-{miesiac:02d}-01'
        ostatni_dzien_miesiaca = f'{rok:04d}-{miesiac:02d}-32'  # tworze str w formacie RRRR-MM-DD
        self.cursor.execute("SELECT * FROM wydatki WHERE data BETWEEN ? AND ? ORDER BY data",
                            (pierwszy_dzien_miesiaca, ostatni_dzien_miesiaca))  # zmienne wskakuja w miejsce znakow ?
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
