from tkinter import *
from tkinter import ttk

# file = open("arquivo.txt", encoding="utf8")
#
# file.read()


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Progressbar()
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()