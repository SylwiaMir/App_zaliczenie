import tkinter as tk
import tkcalendar
from tkinter import ttk
from classes.class_BazaDanych import *
from tkinter import messagebox
from classes.class_Button import CustomButton
from classes.class_Label import CustomLabelSmall, CustomLabel
from classes.class_Entry import CustomEntrySmall

def pokaz_wydatki_gui():
    def zaznaczenie_w_tabeli(event):
        selected_item = table.focus()  # Pobranie zaznaczonego elementu
        values = table.item(selected_item, 'values')  # Pobranie wartości zaznaczonego elementu
        print("Selected Item:", values)
    def pokaz_wszystkie():
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
    def pokaz_wg_miesiąca():
        bazadanych = BazaDanych("wydatki.db")
        bazadanych.utworz_bd()

        while True:
            try:
                rok = rok_entry.get()
                if len(rok) != 4:
                    tk.messagebox.showerror('Błąd', "Wybrano nieprawidłową wartość.")
                    break
                else:
                    rok = int(rok)
                break
            except ValueError:
                tk.messagebox.showerror('Błąd', "Wybrano nieprawidłową wartość.")
                continue
        dict_miesiac = {'01': 'styczeń', '02': 'luty', '03': 'marzec', '04': 'kwiecień', '05': 'maj', '06': 'czerwiec',
                        '07': 'lipiec', '08': 'sierpień', '09': 'wrzesień', '10': 'październik', '11': 'listopad',
                        '12': 'grudzień'}


        miesiac_str = wybierz_miesiac_combobox.get()
        if miesiac_str in dict_miesiac.values():
            miesiac = int([key for key,value in dict_miesiac.items() if value == miesiac_str][0])
        else:
            tk.messagebox.showerror('Błąd', "Wybrano błędny miesiąc.")


        sortowane_dane = bazadanych.sortuj_wg_miesiaca(rok, miesiac)

        # ta czesc kodu wypisuje wydatki na konsoli
        # for row in sortowane_dane:
        #     print(row)

        for item in table.get_children():
            table.delete(item)

        for row in sortowane_dane:
            table.insert('', 'end', values=row)
    def pokaz_wg_daty():
        bazadanych = BazaDanych('wydatki.db')
        bazadanych.utworz_bd()


        data_poczatkowa = data_poczatkowa_dateentry.get()

        data_koncowa = data_koncowa_dateentry.get()

        sortowane_dane = bazadanych.sortuj_wg_zakresu_dat(data_poczatkowa, data_koncowa)

        for item in table.get_children():
            table.delete(item)
        for row in sortowane_dane:
            table.insert('','end', values=row)

    def powrot():
        root.destroy()

    root = tk.Tk()
    root.title("Pokaż wydatki")
    root.geometry("770x660")
    root.configure(bg='#333333')

    frame = tk.Frame(root, background='#333333')
    frame.pack(pady=15)

    pokaz_wydatki_frame = tk.LabelFrame(frame, text="Pokaż wydatki", background='#333333', foreground='#04BFBF',font=('Agenor Neue', 10))
    pokaz_wydatki_frame.grid(row=0, column=0)

    wszystkie_wydatki = CustomButton(pokaz_wydatki_frame, text="Pokaż wszystkie", command= pokaz_wszystkie)
    wszystkie_wydatki.grid(row=4, column=0, padx=(20,30), pady=(0,10))

    sort_data_label = CustomLabel(pokaz_wydatki_frame, text="Wybierz wydatki\nwg daty")
    sort_data_label.grid(row=0, column=1, columnspan=2, padx=(5,30))

    sort_miesiac_label = CustomLabel(pokaz_wydatki_frame, text="Wybierz wydatki\nz miesiąca")
    sort_miesiac_label.grid(row=0, column=3, columnspan=2, padx=(5,10))
    miesiac = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj',  'czerwiec', 'lipiec',
               'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']
    wybierz_miesiac_label = CustomLabelSmall(pokaz_wydatki_frame, text='Wybierz miesiąc')
    wybierz_miesiac_label.grid(row=2, column=3, padx=(5,0))
    wybierz_miesiac_combobox = ttk.Combobox(pokaz_wydatki_frame, values=miesiac, font=('Arial', 10),
                                         width=13, justify='center')
    wybierz_miesiac_combobox.grid(row=2, column=4, padx=(5,20))

    rok_label = CustomLabelSmall(pokaz_wydatki_frame, text='Wpisz rok')
    rok_label.grid(row=3, column=3, padx=(5, 0))

    default_year = "2023"
    rok_entry = CustomEntrySmall(pokaz_wydatki_frame)
    rok_entry.grid(row=3, column=4, padx=(0, 20), pady=10)
    rok_entry.insert(0, default_year)




    wybierz_button = CustomButton(pokaz_wydatki_frame, text="Pokaż z miesiąca", command=pokaz_wg_miesiąca)
    wybierz_button.grid(row=4, column=3, columnspan=2, padx=(5,10),pady=(0,10))

    data_poczatkowa = CustomLabelSmall(pokaz_wydatki_frame, text= "Data początkowa")
    data_poczatkowa.grid(row=2, column=1, padx=5)

    data_poczatkowa_dateentry = tkcalendar.DateEntry(pokaz_wydatki_frame,width=15, background='#04BFBF', foreground='#333333', borderwidth=5,
                           date_pattern='yyyy-mm-dd')
    data_poczatkowa_dateentry.grid(row=2, column=2,padx=(0,20))

    data_koncowa = CustomLabelSmall(pokaz_wydatki_frame, text="Data końcowa")
    data_koncowa.grid(row=3, column=1)

    data_koncowa_dateentry = tkcalendar.DateEntry(pokaz_wydatki_frame,width=15, background='#04BFBF', foreground='#333333', borderwidth=5,
                           date_pattern='yyyy-mm-dd')
    data_koncowa_dateentry.grid(row=3, column=2, padx=(0, 20))


    wybierz_button2 = CustomButton(pokaz_wydatki_frame, text="Pokaż wg daty", command=pokaz_wg_daty)
    wybierz_button2.grid(row=4, column=1, columnspan=2, padx=(5, 10),pady=(0,10))


    table_frame = tk.LabelFrame(frame, text="Wydatki ",background='#333333', foreground='#04BFBF',font=('Agenor Neue', 10,))
    table_frame.grid(row=1, column=0, padx=(10,10), pady=20)

    columns = ('id', 'nazwa', 'kwota', 'data', 'kategoria')

    table = ttk.Treeview(table_frame, columns=columns, show="headings")

    table.heading('id', text="ID")
    table.heading('nazwa', text="Nazwa paragonu")
    table.heading('kwota', text="Kwota")
    table.heading('data', text="Data zakupu")
    table.heading('kategoria', text="Kategoria")

    table.column('id', width=40, anchor="center")
    table.column('nazwa', width=165, anchor="center")
    table.column('kwota', width=105, anchor="center")
    table.column('data', width=185, anchor="center")
    table.column('kategoria', width=205, anchor="center")

    table.grid(row=0, column=0, columnspan=3, padx=20, pady=10)
    table.bind('<<TreeviewSelect>>', zaznaczenie_w_tabeli)

    powrot_button = CustomButton(table_frame, text='Powrót', command=powrot)
    powrot_button.grid(row=1, column=0, columnspan=3, padx=35, pady=10, sticky='e')

    root.mainloop()

pokaz_wydatki_gui()