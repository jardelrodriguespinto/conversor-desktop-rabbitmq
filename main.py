from tkinter import *
from tkinter import ttk
import os
from tkinter import filedialog

from conversion.jpg_conversion import JPGConversion
from conversion.pdf_conversion import PDFConversion
from conversion.png_conversion import PNGConversion
from conversion.txt_conversion import TXTConversion
from conversion.webp_conversion import WEBPConversion
from enum import Enum

class FileExtention(Enum):
    PDF = ".pdf"
    JPG = ".jpg"
    PNG = ".png"
    WEBP = ".webp"
    TXT = ".txt"

def get_file_extention(file):
    return os.path.splitext(file)[1]

def set_option_by_file_extension(file_extention):
    options = []

    if (file_extention == FileExtention.PNG.value):
        options = ["JPG", "BMP", "WEBP"]
    elif(file_extention == FileExtention.JPG.value):
        options = ["PNG", "BMP", "WEBP"]
    elif(file_extention == FileExtention.WEBP.value):
        options = ["PNG", "JPG"]
    elif(file_extention == FileExtention.PDF.value):
        options = ["PNG", "TXT"]
    elif(file_extention == FileExtention.TXT.value):
        options = ["PDF"]

    return options

def convert_file(file, file_extention, desired_option):



    if (file_extention == FileExtention.PNG.value):
        PNGConversion.convert(file, file_extention, desired_option)
    elif(file_extention == FileExtention.JPG.value):
        JPGConversion.convert(file, file_extention, desired_option)
    elif(file_extention == FileExtention.WEBP.value):
        WEBPConversion.convert(file, file_extention, desired_option)
    elif(file_extention == FileExtention.PDF.value):
        PDFConversion.convert(file, file_extention, desired_option)
    elif(file_extention == FileExtention.TXT.value):
        TXTConversion.convert(file, file_extention, desired_option)


def open_explorer():
    file = filedialog.askopenfilename()

    file_extention = get_file_extention(file)

    if any(file_extention == ext.value for ext in FileExtention):

        ttk.Label(frm, text="Tipo de conversão:").grid(column=0, row=0, sticky="w")
        options = set_option_by_file_extension(file_extention)
        combo = ttk.Combobox(frm, values=options, state="readonly")
        combo.grid(column=1, row=0)
        combo.current(0)

        desired_option = combo.get()

        ttk.Button(frm, text="Converter", command=convert_file(file, file_extention, desired_option)).grid(column=4, row=0, pady=20)

    else:
        print("Formato não suportado")

root = Tk()
frm = ttk.Frame(root, padding=100)

frm.grid()

ttk.Progressbar().location(10, 10)

label = ttk.Label(frm, text="Selecione um arquivo que deseja converter:").grid(column=10, row=0, sticky="w", pady=10)
button = ttk.Button(frm, text="Carregar arquivo", command=open_explorer).grid(column=10, row=2)

root.mainloop()

