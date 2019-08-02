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

from BotonAvanzarNumeroSuerte import BotonAvanzarNumeroSuerte

from etiquetaBinarioNumeroSuerte import etiquetaBinarioNumeroSuerte
from etiquetaExadecimalNumeroSuerte import etiquetaExadecimalNumeroSuerte
from cuadroTextoExadecimalNumeroSuerte import cuadroTextoExadecimalNumeroSuerte
from cuadroTextoBinarioNumeroSuerte import cuadroTextoBinarioNumeroSuerte
from cuadroTextoDecimalNumeroSuerte import cuadroTextoDecimalNumeroSuerte
from cuadroTextoLetraNumeroSuerte import cuadroTextoLetraNumeroSuerte
from etiquetaDecimalNumeroSuerte import etiquetaDecimalNumeroSuerte
from etiquetaLetraNumeroSuerte import etiquetaLetraNumeroSuerte
from NumeroSuerte import NumeroSuerte

class ventanaPrincipal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Numero de Fibonacci")
        self.ventana.geometry('800x800')
        self.ventana.config(bg = 'black')

        #componentes Numero Fibonacci
        self.etiquetaFibonacci = Label(self.ventana, text="Numero de Fibonacci",fg="white",bg="black").pack()
        self.numeroF = NumeroFibonacci.NumeroFibonacci()
        self.etiquetaDecimal = etiquetaDecimal(self.ventana)
        self.cuadroTextoDecimal = cuadroTextoDecimal(self.ventana)
        self.etiquetabinario = etiquetaBinario(self.ventana)
        self.cuadroTextobinario = cuadroTextoBinario(self.ventana)
        self.etiquetaexadecimal = etiquetaExadecimal(self.ventana)
        self.cuadroTetoexadecimal = cuadroTextoExadecimal(self.ventana)
        self.etiquetaLetra = etiquetaLetra(self.ventana)
        self.cuadroTextoLetra = cuadroTextoLetra(self.ventana)
        self.botonAvanzar = BotonAvanzar(self.numeroF,self.cuadroTextobinario,self.cuadroTetoexadecimal,self.cuadroTextoDecimal,self.cuadroTextoLetra)
        
        self.etiquetaExtra = Label(self.ventana, text="",fg="white",bg="black").pack()
        
        
        #componentes Numero de la Suerte
        self.etiquetaNumeroSuerte = Label(self.ventana, text="Numero de la suerte",fg="white",bg="black").pack()
        self.numeroS = NumeroSuerte.NumeroSuerte()
        self.etiquetaDecimalNumeroSuerte = etiquetaDecimalNumeroSuerte(self.ventana)
        self.cuadroTextoDecimalNumeroSuerte = cuadroTextoDecimalNumeroSuerte(self.ventana)
        self.etiquetabinarioNumeroSuerte = etiquetaBinarioNumeroSuerte(self.ventana)
        self.cuadroTextoBinarioNumeroSuerte = cuadroTextoBinarioNumeroSuerte(self.ventana)
        self.etiquetaxadecimalNumeroSuerte = etiquetaExadecimalNumeroSuerte(self.ventana)
        self.cuadroTextoExadecimalNumeroSuerte = cuadroTextoExadecimalNumeroSuerte(self.ventana)
        self.etiquetaLetraNumeroSuerte = etiquetaLetraNumeroSuerte(self.ventana)
        self.cuadroTextoLetraNumeroSuerte = cuadroTextoLetraNumeroSuerte(self.ventana)
        self.botonAvanzarNumeroSuerte = BotonAvanzarNumeroSuerte(self.numeroS,self.cuadroTextoBinarioNumeroSuerte,self.cuadroTextoExadecimalNumeroSuerte,self.cuadroTextoDecimalNumeroSuerte,self.cuadroTextoLetraNumeroSuerte)
        self.etiquetaExtra2 = Label(self.ventana, text="",fg="white",bg="black").pack()
        self.botonRetroceder = BotonRetroceder(self.numeroF,self.cuadroTextobinario,self.cuadroTetoexadecimal,self.cuadroTextoDecimal,self.cuadroTextoLetra)
        
        self.ventana.mainloop()


        

