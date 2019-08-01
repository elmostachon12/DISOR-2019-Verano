from tkinter import *
class BotonAvanzar:
    def __init__(self,numeroF,textoBinario,textoExadecimal):
        self.textoBinario=textoBinario
        self.textoExadecimal=textoExadecimal
        self.numeroF = numeroF
        self.boton = Button(None, text='Avanzar',command=self.avanzarNumeroFibonacci)
        self.boton.pack()
    
    def avanzarNumeroFibonacci(self):
        try:
            Fibonacci = self.numeroF
        except:
            print("Modulo no invocable")
        if(Fibonacci.getValor()%2 == 0):
            self.textoBinario.cambiarColor("gray")
            self.textoExadecimal.cambiarColor("gray")
        if(Fibonacci.getValor()%2 == 1):
            self.textoBinario.cambiarColor("blue")
            self.textoExadecimal.cambiarColor("blue")
        Fibonacci.avanzar()
        self.textoBinario.cambiarTexto(Fibonacci.getNumeroBinario())
        self.textoExadecimal.cambiarTexto(Fibonacci.getNumeroHexadecimal())
        
        
        