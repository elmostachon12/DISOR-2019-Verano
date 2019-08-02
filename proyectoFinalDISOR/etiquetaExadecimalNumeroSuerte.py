from tkinter import *
class etiquetaExadecimalNumeroSuerte:
    def __init__(self,master):
        self.master = master
        self.etiquetaExadecimal = Label(master, text="Numero en Hexadecimal")
        self.etiquetaExadecimal.pack()
