import tkinter as tk


class CustomLabelMainManu(tk.Label):
    def __init__(self, master=None, **kwargs):
        tk.Label.__init__(self, master, **kwargs)
        self.configure(
            foreground='#04BFBF',
            background='#333333',
            font=('Agenor Neue', 20,)
        )

class CustomLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        tk.Label.__init__(self, master, **kwargs)
        self.configure(
            foreground='#04BFBF',
            background='#333333',
            font=('Agenor Neue', 16,)
        )
