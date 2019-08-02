from tkinter import *
from BotonAvanzar import BotonAvanzar
from BotonRetroceder import BotonRetroceder
from etiquetaBinario import etiquetaBinario
from etiquetaExadecimal import etiquetaExadecimal
from cuadroTextoExadecimal import cuadroTextoExadecimal
from cuadroTextoBinario import cuadroTextoBinario
from cuadroTextoDecimal import cuadroTextoDecimal
from cuadroTextoLetra import cuadroTextoLetra
from etiquetaDecimal import etiquetaDecimal
from etiquetaLetra import etiquetaLetra
from numeroFibonacci import NumeroFibonacci

class ventanaPrincipal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Numero de Fibonacci")
        self.ventana.geometry('600x800')
        self.ventana.config(bg = 'black')

        #componentes Numero Fibonacci
        self.numeroF = NumeroFibonacci.NumeroFibonacci()
        self.etiquetaDecimal = etiquetaDecimal(self.ventana)
        self.cuadroTextoDecimal = cuadroTextoDecimal(self.ventana)
        self.etiquetabinario = etiquetaBinario(self.ventana)
        self.cuadroTextobinario = cuadroTextoBinario(self.ventana)
        self.etiquetaxadecimal = etiquetaExadecimal(self.ventana)
        self.cuadroTetoexadecimal = cuadroTextoExadecimal(self.ventana)
        self.etiquetaLetra = etiquetaLetra(self.ventana)
        self.cuadroTextoLetra = cuadroTextoLetra(self.ventana)
        self.botonAvanzar = BotonAvanzar(self.numeroF,self.cuadroTextobinario,self.cuadroTetoexadecimal,self.cuadroTextoDecimal,self.cuadroTextoLetra)
        self.botonRetroceder = BotonRetroceder(self.numeroF,self.cuadroTextobinario,self.cuadroTetoexadecimal,self.cuadroTextoDecimal,self.cuadroTextoLetra)
        self.ventana.mainloop()

        

