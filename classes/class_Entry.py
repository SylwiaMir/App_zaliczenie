import tkinter as tk


class CustomEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        tk.Entry.__init__(self, master, **kwargs)
        self.configure(
            width=15,
            background='white',
            justify='center',
            font=('Agenor Neue', 12,)
        )

class CustomEntrySmall(tk.Entry):
    def __init__(self, master=None, **kwargs):
        tk.Entry.__init__(self, master, **kwargs)
        self.configure(
            width=10,
            background='white',
            justify='center',
            font=('Agenor Neue', 12,)
        )