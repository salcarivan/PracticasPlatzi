class Coche ():
    def __init__(self):
     self.largochasis=250
     self.anchoChasis=120
     self.__ruedas=4
     self.__enmarcha=False

    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos
        if (self.__enmarcha):
            chequeo=self.__chequeoint()
        if (self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo, no podemos arrrancar"
        else:
            return "El coche está parado"

    def estado(self):
       print("El cocne tiene ", self.__ruedas, "ruedas. Un ancho de  ",self.anchoChasis, "y un largo de  ",
       self.largochasis)

    def __chequeoint(self):
        print("Realizando chequeo interno")
        self.gasolina="OK"
        self.aceite="Mal"
        self.puertas="cerradas"

        if(self.gasolina=="OK"and self.aceite=="OK"and self.puertas=="cerradas"):
            return True
        else:
            return False

Fiatcoche=Coche()
print(Fiatcoche.arrancar(True))
Fiatcoche.estado()

print ("-------------A continuación creamos el segundo objeto-------- ")

Seatcoche=Coche()
print(Seatcoche.arrancar(False))
Seatcoche.estado()
