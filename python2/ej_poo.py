class Coche ():
    largochasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

    def arrancar(self):
        self.enmarcha=True
    def estado(self):
        if (self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"
michoche=Coche()

print("El largo del coche es: ",michoche.largochasis)
print("El coche tiene",michoche.ruedas,"ruedas")
michoche.arrancar()
print (michoche.estado())