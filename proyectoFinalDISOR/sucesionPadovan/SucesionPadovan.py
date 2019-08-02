import math
import subprocess
class SucesionPadovan:
    def __init__(self):
        self.valor=1
        self.numeroVecesActualizado = 0
        self.binario='0'
        self.hexadecimal='0'
        self.MAX_NUMERO = 999999999999

        self.UNIDADES = (
            'cero',
            'uno',
            'dos',
            'tres',
            'cuatro',
            'cinco',
            'seis',
            'siete',
            'ocho',
            'nueve'
            )

        self.DECENAS = (
            'diez',
            'once',
            'doce',
            'trece',
            'catorce',
            'quince',
            'dieciseis',
            'diecisiete',   
            'dieciocho',
            'diecinueve'
            )

        self.DIEZ_DIEZ = (
            'cero',
            'diez',
            'veinte',
            'treinta',
            'cuarenta',
            'cincuenta',
            'sesenta',
            'setenta',
            'ochenta',
            'noventa'
            )

        self.CIENTOS = (
        '_',
        'ciento',
        'doscientos',
        'trescientos',
        'cuatroscientos',
        'quinientos',
        'seiscientos',
        'setecientos',
        'ochocientos',
        'novecientos'
        )

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

    def numero_a_letras(self,numero):
        numero_entero = int(numero)
        if numero_entero > self.MAX_NUMERO:
            raise OverflowError('Número demasiado alto')
        if numero_entero < 0:
            return 'menos %s' % self.numero_a_letras(abs(numero))
        letras_decimal = ''
        parte_decimal = int(round((abs(numero) - abs(numero_entero)) * 100))
        if parte_decimal > 9:
            letras_decimal = 'punto %s' % self.numero_a_letras(parte_decimal)
        elif parte_decimal > 0:
            letras_decimal = 'punto cero %s' % self.numero_a_letras(parte_decimal)
        if (numero_entero <= 99):
            resultado = self.leer_decenas(numero_entero)
        elif (numero_entero <= 999):
            resultado = self.leer_centenas(numero_entero)
        elif (numero_entero <= 999999):
            resultado = self.leer_miles(numero_entero)
        elif (numero_entero <= 999999999):
            resultado = self.leer_millones(numero_entero)
        else:
            resultado = self.leer_millardos(numero_entero)
        resultado = resultado.replace('uno mil', 'un mil')
        resultado = resultado.strip()
        resultado = resultado.replace(' _ ', ' ')
        resultado = resultado.replace('  ', ' ')
        if parte_decimal > 0:
            resultado = '%s %s' % (resultado, letras_decimal)
        return resultado

    def leer_decenas(self,numero):
        if numero < 10:
            return self.UNIDADES[numero]
        decena, unidad = divmod(numero, 10)
        if numero <= 19:
            resultado = self.DECENAS[unidad]
        elif numero <= 29:
            resultado = 'veinti%s' % self.UNIDADES[unidad]
        else:
            resultado = self.DIEZ_DIEZ[decena]
            if unidad > 0:
                resultado = '%s y %s' % (resultado, self.UNIDADES[unidad])
        return resultado

    def leer_centenas(self,numero):
        centena, decena = divmod(numero, 100)
        if numero == 0:
            resultado = 'cien'
        else:
            resultado = self.CIENTOS[centena]
            if decena > 0:
                resultado = '%s %s' % (resultado, self.leer_decenas(decena))
        return resultado

    def leer_miles(self,numero):
        millar, centena = divmod(numero, 1000)
        resultado = ''
        if (millar == 1):
            resultado = ''
        if (millar >= 2) and (millar <= 9):
            resultado = self.UNIDADES[millar]
        elif (millar >= 10) and (millar <= 99):
            resultado = self.leer_decenas(millar)
        elif (millar >= 100) and (millar <= 999):
            resultado = self.leer_centenas(millar)
        resultado = '%s mil' % resultado
        if centena > 0:
            resultado = '%s %s' % (resultado, self.leer_centenas(centena))
        return resultado

    def leer_millones(self,numero):
        millon, millar = divmod(numero, 1000000)
        resultado = ''
        if (millon == 1):
            resultado = ' un millon '
        if (millon >= 2) and (millon <= 9):
            resultado = self.UNIDADES[millon]
        elif (millon >= 10) and (millon <= 99):
            resultado = self.leer_decenas(millon)
        elif (millon >= 100) and (millon <= 999):
            resultado = self.leer_centenas(millon)
        if millon > 1:
            resultado = '%s millones' % resultado
        if (millar > 0) and (millar <= 999):
            resultado = '%s %s' % (resultado, self.leer_centenas(millar))
        elif (millar >= 1000) and (millar <= 999999):
            resultado = '%s %s' % (resultado, self.leer_miles(millar))
        return resultado

    def leer_millardos(self,numero):
        millardo, millon = divmod(numero, 1000000)
        return '%s millones %s' % (self.leer_miles(millardo), self.leer_millones(millon))

        
    def getValor(self):
        return self.valor

    def getNumeroBinario(self):
        return self.binario

    def getNumeroHexadecimal(self):
        return self.hexadecimal



 

