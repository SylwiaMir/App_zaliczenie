import tkinter as tk
from dodaj_wydatek_gui import *
from funkcje import *
from class_BazaDanych import *
from class_Button import CustomButton
from class_Label import CustomLabel, CustomLabelMainManu


window = tk.Tk()
window.title("Ogarniam wydatki")
window.geometry("670x460")
window.configure(bg='#333333')


main_manu = tk.Frame(window, background='#333333')
main_manu.configure(width=220, height=740)
main_manu.pack(side=tk.LEFT, padx=15, pady=15)

main_manu_label = CustomLabelMainManu(main_manu, text="Co robimy?")
main_manu_label.grid(row=0, column=1, pady=(10,10))

main_frame = tk.Frame(window, background='#333333', width=430, height=740) #bd=1, relief=tk.SOLID
main_frame.pack(side=tk.LEFT, padx=20, pady=20)



menu_buttons = [
    ("Dodaj wydatek", dodaj_wydatek_gui),
    ("Pokaż wydatki", pokaz_wydatki),
    ("Edytuj wydatki", edytuj_wydatki),
    ("Sortowanie", sortuj_wg_miesiaca_menu),
    ("Suma wydatków", sortuj_wg_miesiaca_menu),
    ("Wyjście", window.destroy)]

row_num = 1
for text, command in menu_buttons:
    button = CustomButton(master=main_manu, text=text, command=command)
    button.grid(row=row_num, column=1, pady=5)
    row_num += 1



window.mainloop()
