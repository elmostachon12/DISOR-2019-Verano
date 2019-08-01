import math
import subprocess
class SucesionPadovan:
    def __init__(self):
        self.valor=1
        self.numeroVecesActualizado = 0
        self.binario='0'
        self.hexadecimal='0'

    def avanzar(self):
        a=1
        b=1
        c=1
        i=3
        while(i<=self.numeroVecesActualizado):
            self.valor=a+b
            a=b
            b=c
            c=self.valor
            i=i+1
        self.numeroVecesActualizado += 1

    
    def retroceder(self):
        a=1
        b=1
        c=1
        i=3
        self.numeroVecesActualizado -= 1
        self.valor=1
        while(i<=self.numeroVecesActualizado):
            self.valor=a+b
            a=b
            b=c
            c=self.valor
            i=i+1

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

sucesion = SucesionPadovan()
sucesion.avanzar()

print(sucesion.getValor())


 

