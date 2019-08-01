from tkinter import *
class etiquetaBinario:
    def __init__(self,master):
        self.master=master
        self.etiquetaBinario = Label(self.master, text="Numero en Binario")
        self.etiquetaBinario.grid(row=0,column = 0)
        self.etiquetaBinario.pack()
        


