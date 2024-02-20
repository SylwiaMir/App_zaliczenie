import tkinter as tk

class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        tk.Button.__init__(self, master, **kwargs)
        self.configure(
            width=15,
            height=1,
            font=('Agenor Neue', 13),
            foreground='#333333',
            background='#04BFBF',
            activebackground='#027D7D',
        )
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
    def on_enter(self, event):
        self.config(background='#027D7D')
    def on_leave(self, event):
        self.config(background='#04BFBF')
