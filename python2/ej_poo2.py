class Coche ():
    def __init__(self):
     self.largochasis=250
     self.anchoChasis=120
     self.ruedas=4
     self.enmarcha=False

    def arrancar(self, arrancamos):
        self.enmarcha=arrancamos
        if (self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"
    def estado(self):
       print("Elcocne tiene ", self.ruedas, "ruedas. Un ancho de  ",self.anchoChasis, "y un largo de  ",
       self.largochasis)
Fiatcoche=Coche()
print(Fiatcoche.arrancar(True))
print (Fiatcoche.estado())

print ("-------------A continuación creamos el segundo objeto-------- ")

Seatcoche=Coche()
print(Seatcoche.arrancar(False))
print (Seatcoche.estado())
