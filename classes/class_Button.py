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
            activebackground='#027D7D',  # Kolor po najechaniu myszą
        )
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    # .bind(<event>, function)  --> event: Oznacza konkretne zdarzenie, które chcemy obsłużyć(np. < Button - 1 > dla lewego
    # przycisku myszy, < Enter > dla najechania myszką, < Key > dla naciśnięcia klawisza itp.).function: To
    # jest funkcja(lub metoda), która zostanie wywołana, gdy zdarzenie nastąpi.
    def on_enter(self, event):
        self.config(background='#027D7D')  # Kolor po najechaniu myszą

    def on_leave(self, event):
        self.config(background='#04BFBF')  # Powrót do pierwotnego koloru po opuszczeniu obszaru
