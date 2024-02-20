from dodaj_wydatek_gui import *
from pokaz_wydatki_gui import *
from edytuj_wydatki_gui import *
from suma_wydatkow_gui import *
from classes.class_Button import CustomButton
from classes.class_Label import CustomLabelMainManu


window = tk.Tk()
window.title("Ogarniam wydatki")
window.geometry("770x660")
window.configure(bg='#333333')

main_manu = tk.Frame(window, background='#333333')
main_manu.configure(width=220, height=740)
main_manu.pack(padx=15, pady=15)

main_manu_label = CustomLabelMainManu(main_manu, text="Co robimy?")
main_manu_label.grid(row=0, column=1, pady=(10, 10))

menu_buttons = [
    ("Dodaj wydatek", dodaj_wydatek_gui),
    ("Pokaż wydatki", pokaz_wydatki_gui),
    ("Edytuj wydatki", edytuj_wydatki_gui),
    ("Suma wydatków", suma_wydatkow_gui),
    ("Wyjście", window.destroy)]

row_num = 1
for text, command in menu_buttons:
    button = CustomButton(master=main_manu, text=text, command=command)
    button.grid(row=row_num, column=1, pady=5)
    row_num += 1

window.mainloop()
