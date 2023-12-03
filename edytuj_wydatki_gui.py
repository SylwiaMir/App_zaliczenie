import tkinter as tk
import tkcalendar
from tkinter import ttk
from classes.class_BazaDanych import *
from tkinter import messagebox
from classes.class_Button import CustomButton
from classes.class_Label import CustomLabelSmall, CustomLabel
from classes.class_Entry import CustomEntrySmall, CustomEntry

def edytuj_wydatki_gui():
    def wybor_id():
        try:
            edytuj_id = int(id_entry.get())
            id_entry.destroy()

        except ValueError:
            messagebox.showerror("Błąd","Nieprawidłowa wartość!")

        print(f'Wybrano id: {edytuj_id}')
        print(type(edytuj_id))
        bazadanych = BazaDanych("wydatki.db")
        bazadanych.utworz_bd()

        wybrane_id = bazadanych.wyswietl_wg_id(edytuj_id)

        wybrane_dane = CustomLabel(frame, text=wybrane_id)
        wybrane_dane.grid(row=4, column=0,columnspan=2, pady=5)
        print(wybrane_id)

        stara_nazwa = wybrane_id[1]
        print(stara_nazwa)
        nowa_nazwa = CustomLabelSmall(frame, text="Zmień nazwe:").grid(row=5, column=0, pady=5)
        nowa_nazwa_entry = CustomEntry(frame)
        nowa_nazwa_entry.grid(row=5, column=1, pady=5,)
        nowa_nazwa_entry.insert(0, stara_nazwa)

        stara_kwota = wybrane_id[2]
        nowa_kwota = CustomLabelSmall(frame, text="Zmień kwotę:").grid(row=6, column=0, pady=5)
        nowa_kwota_entry = CustomEntry(frame)
        nowa_kwota_entry.grid(row=6, column=1, pady=5)
        nowa_kwota_entry.insert(0, stara_kwota)

        stara_data = wybrane_id[3]
        nowa_data = CustomLabelSmall(frame, text="Zmień datę:").grid(row=7, column=0, pady=5)
        nowa_data_entry= tkcalendar.DateEntry(frame, width=27, background='#04BFBF', foreground='#333333', borderwidth=5,
                           date_pattern='yyyy-mm-dd')
        nowa_data_entry.grid(row=7, column=1, pady=5)
        nowa_data_entry.delete(0, tk.END)
        nowa_data_entry.insert(0, stara_data)

        stara_kategoria = wybrane_id[4]
        nowa_kategoria = CustomLabelSmall(frame, text="Nowa kategoria:").grid(row=8, column=0, pady=5)
        kategorie_list = ['wydatki podstawowe', 'dom i rachunki', 'rozrywka i podróże', 'zdrowie i uroda',
                          'odzież i obuwie', 'pozostałe']

        nowa_kategoria_combobox = ttk.Combobox(frame, values=kategorie_list, font=('Arial', 12),
                                          width=18, justify='center')
        nowa_kategoria_combobox.set(stara_kategoria)
        nowa_kategoria_combobox.grid(row=8, column=1, pady=(5, 5))


        def nadpisz_dane():
            bazadanych = BazaDanych("wydatki.db")
            try:
                nazwa_wydatku = nowa_nazwa_entry.get()
                kwota_str = nowa_kwota_entry.get().replace(',', '.')
                kwota = float(kwota_str)
                data = nowa_data_entry.get_date().strftime("%Y-%m-%d")
                kategoria = nowa_kategoria_combobox.get()
                if kategoria in kategorie_list and isinstance(kwota, float):
                    bazadanych.update_nazwa(edytuj_id, nazwa_wydatku)
                    bazadanych.update_kwota(edytuj_id, kwota)
                    bazadanych.update_data(edytuj_id,data)
                    bazadanych.update_kategoria(edytuj_id, kategoria)

                    tk.messagebox.showinfo("Zaktualizowano dane", f"""{nazwa_wydatku}
{kwota}
{data}
{kategoria}""")
                    root.destroy()

                elif isinstance(kwota, float):
                    tk.messagebox.showwarning("Błąd", "Nieprawidłowa kategoria!")
                else:
                    tk.messagebox.showwarning("Błąd", "Nieprawidłowa kwota!")
            except:
                tk.messagebox.showwarning("Błąd", "Nieprawidłowa kwota!")


        zatwierdz_button = CustomButton(frame, text="Zatwierdź", command=nadpisz_dane)
        zatwierdz_button.grid(row=11, column=0, columnspan=2, pady=10)

    def powrot():
        root.destroy()


    root = tk.Tk()
    root.title("Edytuj wydatki")
    root.geometry("770x660")
    root.configure(bg='#333333')

    frame = tk.Frame(root, background='#333333')
    frame.pack(pady=15)

    id_label = CustomLabel(frame, text="Wybierz ID\nwydatku do edycji:")
    id_label.grid(row=0, column=0, columnspan=2, pady=(30,0))
    id_entry = CustomEntry(frame)
    id_entry.grid(row=1, column=0, columnspan=2, pady=15)

    wybierz_button = CustomButton(frame, text="Wybierz", command=wybor_id)
    wybierz_button.grid(row=2, column=0,columnspan=2, pady=5)

    powrot_button = CustomButton(frame, text='Powrót', command=powrot)
    powrot_button.grid(row=12, column=0, columnspan=2, padx=35, pady=10, sticky='n')




    root.mainloop()


#edytuj_wydatki_gui()