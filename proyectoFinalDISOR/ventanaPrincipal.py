from tkinter import *
from BotonAvanzar import BotonAvanzar
from BotonRetroceder import BotonRetroceder
from etiquetaBinario import etiquetaBinario
from etiquetaExadecimal import etiquetaExadecimal
from cuadroTextoExadecimal import cuadroTextoExadecimal
from cuadroTextoBinario import cuadroTextoBinario
from numeroFibonacci import NumeroFibonacci

class ventanaPrincipal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Numero de Fibonacci")
        self.ventana.geometry('290x150')
        self.ventana.config(bg = 'black')
        self.numeroF = NumeroFibonacci.NumeroFibonacci()
        self.etiquetabinario = etiquetaBinario(self.ventana)
        self.cuadroTextobinario = cuadroTextoBinario(self.ventana)
        self.etiquetaxadecimal = etiquetaExadecimal(self.ventana)
        self.cuadroTetoexadecimal = cuadroTextoExadecimal(self.ventana)
        self.botonAvanzar = BotonAvanzar(self.numeroF,self.cuadroTextobinario,self.cuadroTetoexadecimal)
        self.botonRetroceder = BotonRetroceder(self.numeroF,self.cuadroTextobinario,self.cuadroTetoexadecimal)
        self.ventana.mainloop()

        

