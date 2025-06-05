from tkinter import *
from tkinter import ttk
import os
from tkinter import filedialog
from enum import Enum


# file = open("arquivo.txt", encoding="utf8")
#
# file.read()

class FileExtention(Enum):
    PDF = ".pdf"
    JPG = ".jpg"
    PNG = ".png"
    BMP = ".bmp"
    WEBP = ".webp"
    TXT = ".txt"

def abrir_explorer():
    file = filedialog.askopenfilename()

    if any(file.endswith(ext.value) for ext in FileExtention):
        print(file)
    else:
        print("Formato não suportado")


root = Tk()
frm = ttk.Frame(root, padding=100)

frm.grid()

ttk.Progressbar().location(10, 10)


monthchoosen = ttk.Combobox(frm, width = 270, textvariable = "asd")

# Adding combobox drop down list
monthchoosen['values'] = (' January',
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')

button = ttk.Button(frm, text="Carregar arquivo", command=abrir_explorer).grid(column=1, row=1)




root.mainloop()

