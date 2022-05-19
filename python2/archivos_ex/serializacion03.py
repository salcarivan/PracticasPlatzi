import pickle
class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print("Marca: ",self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",self.enmarcha,
        "\nAcelerando: ", self.acelera, "\nFrenando:", self.frena)

class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if (self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no estacargada"

class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"

    def estado(self):
        print("Marca: ",self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",self.enmarcha,
        "\nAcelerando: ", self.acelera, "\nFrenando:", self.frena,"\n",self.hcaballito)

class VElectricos (Vehiculos):
    def __init__(self,marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia=100
    def cargaEnergia(self):
        self.cargando=True

coche1=Vehiculos("Mazda","MX5")

coche2=Vehiculos("Seat","Leon")

coche3=Vehiculos("Cintroen","C5")

coches=[coche1,coche2,coche3]

fichero=open("loscohes", "wb")

pickle.dump(coches,fichero)

fichero.close()

del (fichero)

leerficehro=open("loscohes","rb")

miscoches=pickle.load(leerficehro)

leerficehro.close()

for c in miscoches:

    print(c.estado())