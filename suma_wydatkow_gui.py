import tkinter as tk
import tkcalendar
from tkinter import ttk
from classes.class_BazaDanych import *
from tkinter import messagebox
from classes.class_Button import CustomButton
from classes.class_Label import CustomLabelSmall, CustomLabel
from classes.class_Entry import CustomEntrySmall

def suma_wydatkow_gui():
    def suma_wydatkow():
        for widget in frame2.winfo_children():
            widget.destroy()

        bazadanych = BazaDanych("wydatki.db")
        bazadanych.utworz_bd()

        suma_wydatkow = bazadanych.suma_wszystkich()

        suma_lbl = CustomLabel(frame2, text="Suma wszystkich\nwydatków:")
        suma_lbl.grid(row=6, column=0, columnspan=5, pady=(20,5))

        suma_wynik = CustomLabel(frame2, text=f"{suma_wydatkow} zł")
        suma_wynik.grid(row=7, column=0, columnspan=5, pady=5)



    def suma_wg_zakresu():
        for widget in frame2.winfo_children():
            widget.destroy()
        bazadanych = BazaDanych("wydatki.db")
        bazadanych.utworz_bd()

        data_poczatkowa = data_poczatkowa_dateentry.get()
        data_koncowa = data_koncowa_dateentry.get()

        suma_wydatkow = bazadanych.suma_z_zakresu(data_poczatkowa, data_koncowa)

        suma_lbl = CustomLabel(frame2, text="Suma wydatków\nz wybranego okresu:")
        suma_lbl.grid(row=6, column=0, columnspan=5, pady=(20,5))

        suma_wynik = CustomLabel(frame2, text=f"{suma_wydatkow} zł")
        suma_wynik.grid(row=7, column=0, columnspan=5, pady=5)

    def suma_z_miesiaca():

        for widget in frame2.winfo_children():
            widget.destroy()
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
            miesiac = int([key for key, value in dict_miesiac.items() if value == miesiac_str][0])
        else:
            tk.messagebox.showerror('Błąd', "Wybrano błędny miesiąc.")


        suma_wydatkow = bazadanych.suma_z_miesiaca(rok, miesiac)

        suma_lbl = CustomLabel(frame2, text="Suma wydatków\nz wybranego miesiaca:")
        suma_lbl.grid(row=6, column=0, columnspan=5, pady=(20,5))

        suma_wynik = CustomLabel(frame2, text=f"{suma_wydatkow} zł")
        suma_wynik.grid(row=7, column=0, columnspan=5, pady=5)



    def powrot():
        root.destroy()


    root = tk.Tk()
    root.title("Suma wydatków")
    root.geometry("770x660")
    root.configure(bg='#333333')

    frame = tk.Frame(root, background='#333333')
    frame.pack(pady=15)

    frame2 = tk.Frame(root, bg='#333333')
    frame2.pack(pady=15)

    #wyświetl wszystkie wydatki
    wszystkie_wydatki = CustomButton(frame, text="Suma wszystkich", command=suma_wydatkow)
    wszystkie_wydatki.grid(row=4, column=0, padx=(20, 30), pady=(0, 10))

    #wyświetl wydatki z zakresu dat
    sort_data_label = CustomLabel(frame, text="Suma wydatków\nwg daty")
    sort_data_label.grid(row=0, column=1, columnspan=2, padx=(5, 30), pady=(25, 0))

    data_poczatkowa = CustomLabelSmall(frame, text="Data początkowa")
    data_poczatkowa.grid(row=2, column=1, padx=5)

    data_poczatkowa_dateentry = tkcalendar.DateEntry(frame, width=15, background='#04BFBF',
                                                     foreground='#333333', borderwidth=5,
                                                     date_pattern='yyyy-mm-dd')
    data_poczatkowa_dateentry.grid(row=2, column=2, padx=(0, 20))

    data_koncowa = CustomLabelSmall(frame, text="Data końcowa")
    data_koncowa.grid(row=3, column=1)

    data_koncowa_dateentry = tkcalendar.DateEntry(frame, width=15, background='#04BFBF',
                                                  foreground='#333333', borderwidth=5,
                                                  date_pattern='yyyy-mm-dd')
    data_koncowa_dateentry.grid(row=3, column=2, padx=(0, 20))

    wybierz_button2 = CustomButton(frame, text="Pokaż wg daty", command=suma_wg_zakresu)
    wybierz_button2.grid(row=4, column=1, columnspan=2, padx=(5, 10), pady=(0, 10))



    #wyświetl wydatki z wybranego miesiąca
    sort_miesiac_label = CustomLabel(frame, text="Suma wydatków\nz wybranego miesiąca")
    sort_miesiac_label.grid(row=0, column=3, columnspan=2, padx=(5, 10), pady=(25,0))

    miesiac = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec',
               'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']
    wybierz_miesiac_label = CustomLabelSmall(frame, text='Wybierz miesiąc')
    wybierz_miesiac_label.grid(row=2, column=3, padx=(5, 0))
    wybierz_miesiac_combobox = ttk.Combobox(frame, values=miesiac, font=('Arial', 10),
                                            width=13, justify='center')
    wybierz_miesiac_combobox.grid(row=2, column=4, padx=(5, 20))

    rok_label = CustomLabelSmall(frame, text='Wpisz rok')
    rok_label.grid(row=3, column=3, padx=(5, 0))

    default_year = "2023"
    rok_entry = CustomEntrySmall(frame)
    rok_entry.grid(row=3, column=4, padx=(0, 20), pady=10)
    rok_entry.insert(0, default_year)

    wybierz_button = CustomButton(frame, text="Suma wg miesiąca", command=suma_z_miesiaca)
    wybierz_button.grid(row=4, column=3, columnspan=2, padx=(5, 10), pady=(0, 10))




    powrot_button = CustomButton(root, text='Powrót', command=powrot)
    powrot_button.pack(side="bottom", pady=(0, 40),)

    root.mainloop()


suma_wydatkow_gui()