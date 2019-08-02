from tkinter import *
class BotonAvanzarNumeroSuerte:
    def __init__(self,numeroS,textoBinario,textoExadecimal,textoDecimal,textoLetra):
        self.textoDecimal = textoDecimal
        self.textoBinario=textoBinario
        self.textoExadecimal=textoExadecimal
        self.textoLetra = textoLetra
        self.numeroS = numeroS
        self.boton = Button(None, text='Avanzar',command=self.avanzarNumeroSuerte)
        self.boton.pack()
    
    def avanzarNumeroSuerte(self):
        try:
            Suerte = self.numeroS
        except:
            print("Modulo no invocable")
        Suerte.avanzar()
        self.textoDecimal.cambiarTexto(Suerte.getValor())
        self.textoBinario.cambiarTexto(Suerte.getNumeroBinario())
        self.textoExadecimal.cambiarTexto(Suerte.getNumeroHexadecimal())
        print(Suerte.getNumeroHexadecimal())
        self.textoLetra.cambiarTexto(Suerte.numero_a_letras(Suerte.getValor()))
        
        
        