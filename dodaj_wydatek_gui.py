import tkinter as tk
import tkcalendar
from tkinter import ttk
from classes.class_BazaDanych import *
from tkinter import messagebox
from classes.class_Button import CustomButton
from classes.class_Label import CustomLabel
from classes.class_Entry import CustomEntry

def dodaj_wydatek_gui():
    def dodaj_do_bazy():
        bazadanych = BazaDanych("wydatki.db")
        try:
            nazwa_wydatku = nazwa_entry.get()
            kwota_str = kwota_entry.get().replace(',', '.')
            kwota = float(kwota_str)
            data = data_entry.get_date().strftime("%Y-%m-%d")
            kategoria = kategorie_combobox.get()
            if kategoria in kategorie_list and isinstance(kwota,float):
                bazadanych.dodaj_dane(nazwa_wydatku, kwota, data, kategoria)
                print(f"Dodano nowe dane: {nazwa_wydatku},{kwota},{data},{kategoria}")
                tk.messagebox.showinfo("Dodano dane", f"""{nazwa_wydatku}
{kwota}
{data}
{kategoria}""")
                root.destroy()

            elif isinstance(kwota,float):
                tk.messagebox.showwarning("Błąd", "Nieprawidłowa kategoria!")
            else:
                tk.messagebox.showwarning("Błąd", "Nieprawidłowa kwota!")
        except:
            tk.messagebox.showwarning("Błąd", "Nieprawidłowa kwota!")




    def powrot():
        root.destroy()


    root = tk.Tk()
    root.title("Dodaj Wydatek")
    root.geometry("770x660")
    root.configure(bg='#333333')

    frame = tk.Frame(root, background='#333333')
    frame.pack(pady=15)

    #Nazwy nad polami entry/date/combobox
    CustomLabel(frame,text="Nazwa sklepu:").grid(row=0, column=0, pady=1)
    CustomLabel(frame, text="Kwota paragonu:").grid(row=2, column=0, pady=1)
    CustomLabel(frame, text="Data:").grid(row=4, column=0, pady=0)
    CustomLabel(frame, text="Wybierz kategorie:").grid(row=6, column=0, pady=0)


    nazwa_entry = CustomEntry(frame)
    nazwa_entry.grid(row=1, column=0, pady=5)

    kwota_entry = CustomEntry(frame)
    kwota_entry.grid(row=3, column=0, pady=5)

    data_entry = tkcalendar.DateEntry(frame, width=27, background='#04BFBF', foreground='#333333', borderwidth=5,
                           date_pattern='yyyy-mm-dd')
    data_entry.grid(row=5, column=0, pady=5)

    kategorie_list = ['wydatki podstawowe', 'dom i rachunki', 'rozrywka i podróże', 'zdrowie i uroda',
                      'odzież i obuwie','pozostałe']

    kategorie_combobox = ttk.Combobox(frame, values=kategorie_list, font=('Agenor Neue', 12),
                                         width=13, justify='center')
    kategorie_combobox.set(' ')
    kategorie_combobox.grid(row=7, column=0, pady=(5,30))

    #przyciski dodaj/powrót
    CustomButton(frame, text="Dodaj", command=dodaj_do_bazy).grid(row=8, column=0, columnspan=2, pady=5)
    CustomButton(frame, text="Powrót", command=powrot).grid(row=9, column=0, pady=5)


    root.mainloop()

#dodaj_wydatek_gui()