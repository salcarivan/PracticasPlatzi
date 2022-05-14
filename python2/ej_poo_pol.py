class Coche ():

    def desplazamiento (self):
        print("Me despazo usando 4 ruedas")

class Moto ():

    def desplazamiento (self):
        print("Me despazo usando 2 ruedas")

class Camion ():

    def desplazamiento (self):
        print("Me despazo usando 6 ruedas")

def desplazamientoVehiculo (vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Coche()
desplazamientoVehiculo(miVehiculo)
