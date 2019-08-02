from tkinter import *
class BotonRetroceder:
    def __init__(self,numeroF,textoBinario,textoExadecimal,textoDecimal,textoLetra):
        self.textoBinario=textoBinario
        self.textoExadecimal=textoExadecimal
        self.textoDecimal = textoDecimal
        self.textoLetra = textoLetra
        self.numeroF = numeroF
        self.boton = Button(None, text='Retroceder',command=self.retrocederNumeroFibonacci)
        self.boton.pack()
    

    def retrocederNumeroFibonacci(self):
        try:
            Fibonacci = self.numeroF
        except:
            print("Modulo no invocable")
        self.textoDecimal.cambiarTexto(Fibonacci.getValor())
        self.textoBinario.cambiarTexto(Fibonacci.getNumeroBinario())
        self.textoExadecimal.cambiarTexto(Fibonacci.getNumeroHexadecimal())
        self.textoLetra.cambiarTexto(Fibonacci.numero_a_letras(Fibonacci.getValor()))

        try:
            Fibonacci.retroceder()
        except ValueError as e:
            print(e)

            


        