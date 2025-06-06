from tkinter import *
from tkinter import ttk


root = Tk()
frm = ttk.Frame(root, padding=100)

frm.grid()

ttk.Progressbar().location(10, 10)

label = ttk.Label(frm, text="Selecione um arquivo que deseja converter:").grid(column=10, row=0, sticky="w", pady=10)
button = ttk.Button(frm, text="Carregar arquivo", command=open_explorer).grid(column=10, row=2)

root.mainloop()
