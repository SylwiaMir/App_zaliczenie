import tkinter as tk
import tkcalendar
from tkinter import ttk
from classes.class_BazaDanych import *
from tkinter import messagebox
from classes.class_Button import CustomButton
from classes.class_Label import CustomLabel
from classes.class_Entry import CustomEntry

def pokaz_wydatki_gui():
    def pokaz_wydatki():
        bazadanych = BazaDanych("wydatki.db")
        bazadanych.utworz_bd()

        aktualne_dane = bazadanych.wyswietl_dane()
        # ta czesc kodu wypisuje wydatki na konsoli
        #print("Aktualne wydatki:")
        # for row in aktualne_dane:
        #      print(row)

        for item in table.get_children():
            table.delete(item)

        for row in aktualne_dane:
            table.insert('', 'end', values=row)

    def powrot():
        root.destroy()

    root = tk.Tk()
    root.title("Pokaż wydatki")
    root.geometry("670x460")
    root.configure(bg='#333333')

    frame = tk.Frame(root, background='#333333')
    frame.pack(pady=15)

    pokaz_wydatki_frame = tk.LabelFrame(frame, text="Pokaż wydatki", background='#333333', foreground='#04BFBF',font=('Agenor Neue', 10,))
    pokaz_wydatki_frame.grid(row=0, column=0)

    wszystkie_wydatki = CustomButton(pokaz_wydatki_frame, text="Wszystkie", command= pokaz_wydatki)
    wszystkie_wydatki.grid(row=1, column=0)

    table_frame = tk.LabelFrame(frame, text="Tu bedzie tabela",background='#333333', foreground='#04BFBF',font=('Agenor Neue', 10,))
    table_frame.grid(row=1, column=0, padx=(0,100))

    columns = ('id', 'nazwa', 'kwota', 'data', 'kategoria')

    table = ttk.Treeview(table_frame, columns=columns, show="headings")
    table.heading('id', text="Nazwa paragonu")
    table.heading('nazwa', text="Nazwa paragonu")
    table.heading('kwota', text="Kwota")
    table.heading('data', text="Data zakupu")
    table.heading('kategoria', text="Kategoria")

    table.grid(row=0, column=0, columnspan=3, padx=5, pady=10)

    powrot_button = CustomButton(table_frame, text='Powrót', command=powrot)
    powrot_button.grid(row=1, column=0, columnspan=3, padx=5, pady=10, sticky='s')

    root.mainloop()

#pokaz_wydatki_gui()