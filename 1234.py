import tkinter as tk


def on_id_submit():
    global id_entry
    id_value = id_entry.get()
    #id_entry.destroy()  # Usunięcie pola Entry po zatwierdzeniu ID

    label_new_category = tk.Label(root, text="Wprowadź nową kategorię:")
    label_new_category.pack(pady=10)

    new_category_entry = tk.Entry(root)
    new_category_entry.pack(pady=10)


    submit_button = tk.Button(root, text="Zatwierdź", command=lambda: on_category_submit(new_category_entry))
    submit_button.pack(pady=10)


def on_category_submit(entry):
    new_category_value = entry.get()
    print("ID:", id_value)
    print("Nowa kategoria:", new_category_value)
    root.destroy()


root = tk.Tk()
root.title("Prosty Skrypt")

# Pole Entry do wpisania ID
label_id = tk.Label(root, text="Wybierz ID:")
label_id.pack(pady=10)

id_entry = tk.Entry(root)
id_entry.pack(pady=10)

submit_button = tk.Button(root, text="Zatwierdź", command=on_id_submit)
submit_button.pack(pady=10)

root.mainloop()