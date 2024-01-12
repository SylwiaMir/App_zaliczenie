import tkinter
from funkcje import *
import pytest
from unittest.mock import Mock, patch
from tkinter import Tk
from dodaj_wydatek_gui import *

@pytest.fixture
def app():
    root = Tk()
    yield root
    root.destroy()

def test_dodaj_wydatek_gui(app):
    with patch("classes.class_BazaDanych.BazaDanych") as mock_bazadanych, \
         patch("tkinter.messagebox.showinfo"), \
         patch("tkinter.messagebox.showwarning"), \
         patch("tkinter.Tk.destroy"):

        # Symuluj dane wejściowe
        dodaj_wydatek_gui.nazwa_entry = Mock(get=lambda: "Sklep testowy")
        dodaj_wydatek_gui.kwota_entry = Mock(get=lambda: "100.0")
        dodaj_wydatek_gui.data_entry = Mock(get_date=Mock(return_value="2023-01-01"))
        dodaj_wydatek_gui.kategorie_combobox = Mock(get=lambda: "wydatki podstawowe")

        dodaj_do_bazy = dodaj_wydatek_gui.dodaj_do_bazy

        # Wywołaj funkcję
        dodaj_do_bazy()
        # Sprawdź, czy odpowiednie metody zostały wywołane
        mock_bazadanych.return_value.dodaj_dane.assert_called_once_with(
            "Sklep testowy", 100.0, "2023-01-01", "wydatki podstawowe"
        )
        tkinter.messagebox.showinfo.assert_called_once()
        tkinter.Tk.destroy.assert_called_once()