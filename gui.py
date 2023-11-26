import customtkinter as ctk
from class_BazaDanych import *
window = ctk.CTk()
window.title("Ogarniam wydatki")
window.geometry("440x540")
window.configure(fg_color='#333333')

main_manu = ctk.CTkFrame(window, fg_color='#333333')
main_manu.pack(padx=50, pady= 30)

main_manu_label = ctk.CTkLabel(main_manu,
                               text="Co robimy?",
                               text_color='#04BFBF',
                               fg_color='#333333',
                               bg_color='#333333',
                               font=ctk.CTkFont('Agenor Neue', 38, ))
main_manu_label.grid(row=0, column=1, pady=(15,10))

menu_buttons = [
    ("Dodaj wydatek", dodaj_wydatek),
    ("Pokaż wydatki", pokaz_wydatki),
    ("Edytuj wydatki", edytuj_wydatki),
    ("Sortowanie", sortuj_wg_miesiaca_menu),
    ("Suma wydatków", sortuj_wg_miesiaca_menu),
    ("Wyjście", window.quit)]

row_num = 1
for text, command in menu_buttons:
    button = ctk.CTkButton(master=main_manu,
                           text=text,
                           width=250,
                           height=50,
                           text_color='#333333',
                           fg_color='#04BFBF',
                           hover_color='#027D7D',
                           corner_radius=4,
                           font=ctk.CTkFont('Agenor Neue', 20),
                           command=command)
    button.grid(row=row_num, column=1, pady=5)
    row_num += 1



window.mainloop()
