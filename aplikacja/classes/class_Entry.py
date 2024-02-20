import tkinter as tk

class CustomEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        tk.Entry.__init__(self, master, **kwargs)
        self.configure(
            width=20,
            background='white',
            justify='center',
            font=('Arial', 12,)
        )
class CustomEntrySmall(tk.Entry):
    def __init__(self, master=None, **kwargs):
        tk.Entry.__init__(self, master, **kwargs)
        self.configure(
            width=15,
            background='white',
            justify='center',
            font=('Arial', 10,)
        )