from tkinter import *
from tkinter import ttk
import os
from tkinter import filedialog

# file = open("arquivo.txt", encoding="utf8")
#
# file.read()

def abrir_explorer():
    file = filedialog.askopenfilename()

root = Tk()

frm = ttk.Frame(root, padding=100)

frm.grid()

ttk.Label(frm, text="Abrir Arquivo").grid(column=1, row=0)
ttk.Progressbar().location(10, 10)

button = ttk.Button(frm, text="Carregar arquivo", command=abrir_explorer).grid(column=1, row=1)




root.mainloop()

