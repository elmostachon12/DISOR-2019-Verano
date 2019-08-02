from tkinter import *
class BotonAvanzarNumeroSuerte:
    def __init__(self,numeroF,textoBinario,textoExadecimal,textoDecimal,textoLetra):
        self.textoDecimal = textoDecimal
        self.textoBinario=textoBinario
        self.textoExadecimal=textoExadecimal
        self.textoLetra = textoLetra
        self.numeroF = numeroF
        self.boton = Button(None, text='Avanzar',command=self.avanzarNumeroFibonacci)
        self.boton.pack()
    
    def avanzarNumeroFibonacci(self):
        try:
            Fibonacci = self.numeroF
        except:
            print("Modulo no invocable")
        Fibonacci.avanzar()
        self.textoDecimal.cambiarTexto(Fibonacci.getValor())
        self.textoBinario.cambiarTexto(Fibonacci.getNumeroBinario())
        self.textoExadecimal.cambiarTexto(Fibonacci.getNumeroHexadecimal())
        self.textoLetra.cambiarTexto(Fibonacci.numero_a_letras(Fibonacci.getValor()))
        
        
        