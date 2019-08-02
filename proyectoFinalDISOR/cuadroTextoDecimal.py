from tkinter import *
class cuadroTextoDecimal:
    def __init__(self,master):
        self.master=master
        self.entrada = StringVar()
        self.entrada.set('0')
        self.cuadroTexto = Entry(master,textvariable=self.entrada,fg="white",bg="black")
        self.cuadroTexto.pack()
    
    def cambiarTexto(self,texto):
        if(texto !=''):
            self.entrada.set(texto)
        if(texto ==''):
            self.entrada.set('0')
    
    def cambiarColor(self,color):
        self.cuadroTexto.config(bg = color)
