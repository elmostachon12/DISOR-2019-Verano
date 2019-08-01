from tkinter import *
class BotonRetroceder:
    def __init__(self,numeroF,textoBinario,textoExadecimal):
        self.textoBinario=textoBinario
        self.textoExadecimal=textoExadecimal
        self.numeroF = numeroF
        self.boton = Button(None, text='Retroceder',command=self.retrocederNumeroFibonacci)
        self.boton.pack()
    

    def retrocederNumeroFibonacci(self):
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
        self.textoBinario.cambiarTexto(Fibonacci.getNumeroBinario())
        self.textoExadecimal.cambiarTexto(Fibonacci.getNumeroHexadecimal())
        try:
            Fibonacci.retroceder()
        except ValueError as e:
            print(e)

            


        