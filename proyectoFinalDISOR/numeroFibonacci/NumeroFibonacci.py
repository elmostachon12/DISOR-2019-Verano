import math
import subprocess
class NumeroFibonacci:
    def __init__(self):
        self.numeroAnterior = 0
        self.numeroActual =0
        self.numeroVecesActualizado =0
        self.valor =0
        self.binario='0'
        self.hexadecimal='0'


    def avanzar(self):
        self.numeroVecesActualizado +=1
        if self.numeroVecesActualizado == 0:
            self.numeroAnterior = 0
            self.numeroActual = 1
        if self.numeroVecesActualizado == 1:
            self.terminoAnterior = 1
            self.numeroActual = 1
        if self.numeroVecesActualizado >= 2:
            respaldoNumeroAnterior = self.numeroAnterior
            self.numeroAnterior = self.numeroActual
            self.numeroActual = self.numeroAnterior + respaldoNumeroAnterior
        self.valor = self.numeroActual
        self.binario=''
        self.hexadecimal=''
        self.GenerarNumeroBinario()
        self.GenerarNumeroExadecimal()

    def reiniciar(self):
        self.numeroActual = 0
        self.numeroAnterior = 0
        self.numeroVecesActualizado = 0
        self.valor = 0
        self.binario='0'
        self.hexadecimal='0'

    def retroceder(self):
        if(self.numeroActual <= 0):
            raise ValueError("No se puede retroceder al iniciar o al regresar hasta cero")
            self.reiniciar()
        respaldoNumeroActual = self.numeroActual
        self.numeroActual = self.numeroAnterior
        self.numeroAnterior = respaldoNumeroActual - self.numeroActual
        self.valor = self.numeroActual
        self.numeroVecesActualizado -=1
        self.binario=''
        self.hexadecimal=''
        self.GenerarNumeroBinario()
        self.GenerarNumeroExadecimal()
        

    def GenerarNumeroBinario(self):
        numero = self.valor
        while(numero > 0):
            if(numero %2 ==0):
                self.binario = "0" + self.binario
            else:
                self.binario = "1" + self.binario
            numero = int(math.floor(numero/2))


    def GenerarNumeroExadecimal(self):
        numero = self.valor
        while numero != 0: 
            residuo = self.__CambiarDigitos(numero % 16)
            self.hexadecimal = str(residuo) + self.hexadecimal
            numero = int(numero / 16)            

    def __CambiarDigitos(self,digitos):
        decimales =   [10 , 11 , 12 , 13 , 14 , 15 ]
        hexadecimal = ["A", "B", "C", "D", "E", "F"]
        for caracter in range(7):
            if digitos == decimales[caracter-1]:
                digitos = hexadecimal[caracter-1]
        return digitos
    
    def getValor(self):
        return self.valor

    def getNumeroBinario(self):
        return self.binario

    def getNumeroHexadecimal(self):
        return self.hexadecimal



    