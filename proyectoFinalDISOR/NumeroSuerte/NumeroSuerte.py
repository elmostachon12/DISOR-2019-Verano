class NumeroSuerte:
    def __init__(self):
        self.valor=1
        self.numeroVecesActualizado = 2
        self.binario='0'
        self.hexadecimal='0'

    def avanzar(self):
        List=range(-1,self.numeroVecesActualizado*self.numeroVecesActualizado+9,2)
        i=2
        while List[i:]:
            List=sorted(set(List)-set(List[List[i]::List[i]]));i+=1
        self.valor = List[self.numeroVecesActualizado]
        self.numeroVecesActualizado +=1

    def retroceder(self):
        if(self.numeroVecesActualizado>=2):
            self.numeroVecesActualizado -=1
            List=range(-1,self.numeroVecesActualizado*self.numeroVecesActualizado+9,2)
            i=2
            while List[i:]:
                List=sorted(set(List)-set(List[List[i]::List[i]]));i+=1
            self.valor = List[self.numeroVecesActualizado]
        if(self.numeroVecesActualizado<2):
            self.valor = 1
            self.numeroVecesActualizado =2

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

