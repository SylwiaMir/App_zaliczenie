import customtkinter as ctk
from datetime import datetime
from class_BazaDanych import *
from tkcalendar import DateEntry
from tkinter import messagebox


def dodaj_wydatek_gui():
    def dodaj_do_bazy():

        try:
            nazwa_wydatku = nazwa_entry.get()
            kwota_str = kwota_entry.get().replace(',', '.')
            kwota = float(kwota_str)
            data = data_entry.get_date().strftime("%Y-%m-%d")
            kategoria = kategorie_combobox.get()
            if kategoria in kategorie_list and isinstance(kwota,float):
                bazadanych.dodaj_dane(nazwa_wydatku, kwota, data, kategoria)
                print(f"Dodano nowe dane: {nazwa_wydatku},{kwota},{data},{kategoria}")
                messagebox.showinfo("Dodano dane", f"""{nazwa_wydatku}
{kwota}
{data}
{kategoria}""")
                root.destroy()

            elif isinstance(kwota,float):
                messagebox.showinfo("Błąd", "Nieprawidłowa kategoria!")
            else:
                messagebox.showinfo("Błąd", "Nieprawidłowa kwota!")
        except:
            messagebox.showinfo("Błąd", "Nieprawidłowa kwota!")

    def powrot():
        root.destroy()

    bazadanych = BazaDanych("wydatki.db")

    root = ctk.CTk()
    root.title("Dodaj Wydatek")
    root.geometry("440x540")
    root.configure(fg_color='#333333')

    frame = ctk.CTkFrame(root,
                         fg_color='#333333')
    frame.pack(padx=50, pady=20)

    nazwa_label = ctk.CTkLabel(frame,
                               text="Nazwa sklepu:",
                               text_color='#04BFBF',
                               fg_color='#333333',
                               bg_color='#333333',
                               font=ctk.CTkFont('Agenor Neue', 20, ))
    nazwa_label.grid(row=0, column=1, pady=1)

    nazwa_entry = ctk.CTkEntry(frame,
                               width=250,
                               height=50)
    nazwa_entry.grid(row=1, column=1, pady=10)

    kwota_label = ctk.CTkLabel(frame,
                               text="Kwota paragonu:",
                               text_color='#04BFBF',
                               fg_color='#333333',
                               bg_color='#333333',
                               font=ctk.CTkFont('Agenor Neue', 20, ))
    kwota_label.grid(row=2, column=1, pady=1)

    kwota_entry = ctk.CTkEntry(frame,
                               width=250,
                               height=50)
    kwota_entry.grid(row=3, column=1, pady=10)

    data_label = ctk.CTkLabel(frame,
                              text="Data:",
                              text_color='#04BFBF',
                              fg_color='#333333',
                              bg_color='#333333',
                              font=ctk.CTkFont('Agenor Neue', 20, ))
    data_label.grid(row=4, column=1, pady=0)

    data_entry = DateEntry(frame, width=12, background='#04BFBF', foreground='#333333', borderwidth=5,
                           date_pattern='yyyy-mm-dd')
    data_entry.grid(row=5, column=1, pady=10)

    kategorie_list = ['wydatki podstawowe', 'dom i rachunki', 'rozrywka i podróże', 'zdrowie i uroda',
                      'odzież i obuwie','pozostałe']
    kategorie_label = ctk.CTkLabel(frame,
                                   text="Wybierz kategorie:",
                                   text_color='#04BFBF',
                                   fg_color='#333333',
                                   bg_color='#333333',
                                   font=ctk.CTkFont('Agenor Neue', 20, ))
    kategorie_label.grid(row=6, column=1, pady=0)

    kategorie_combobox = ctk.CTkComboBox(frame,
                                         values=kategorie_list,
                                         font=ctk.CTkFont('Agenor Neue', 16),
                                         width=250,
                                         height=50,
                                         button_color='#027D7D',
                                         button_hover_color='#04BFBF',
                                         dropdown_hover_color='#027D7D',
                                         dropdown_font=ctk.CTkFont('Agenor Neue', 12),
                                         justify='center')
    kategorie_combobox.set(' ')
    kategorie_combobox.grid(row=7, column=1, pady=10)

    dodaj_button = ctk.CTkButton(frame,
                                 text="Dodaj",
                                 width=250,
                                 height=50,
                                 text_color='#333333',
                                 fg_color='#04BFBF',
                                 hover_color='#027D7D',
                                 corner_radius=4,
                                 font=ctk.CTkFont('Agenor Neue', 20),
                                 command=dodaj_do_bazy)
    dodaj_button.grid(row=8, column=1, columnspan=2, pady=5)

    powrot_button = ctk.CTkButton(frame,
                                  text="Powrót",
                                  width=250,
                                  height=50,
                                  text_color='#333333',
                                  fg_color='#04BFBF',
                                  hover_color='#027D7D',
                                  corner_radius=4,
                                  font=ctk.CTkFont('Agenor Neue', 20),
                                  command=powrot)
    powrot_button.grid(row=9, column=1, pady=5)

    root.mainloop()

dodaj_wydatek_gui()
