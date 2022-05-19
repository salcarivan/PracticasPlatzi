import pickle

class Persona:
    
    def __init__(self, nombre,genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class Listapersonas:
    
    personas=[]

    def __init__(self):
         
         listadepersona=open ("ficheroext","ab+")
         listadepersona.seek(0)
 
         try:
            self.personas=pickle.load(listadepersona)
            print("Se cargaron {} personas del fichero del fichero externo".format(len(self.personas)))
         
         except:
             print ("el fichero está vavío")

         finally: 
             listadepersona.close()
             del(listadepersona)

    def agregarPersonas (self, p):
        self.personas.append(p)
        self.guardarpersonasenficheroexterno

    def mostarpersonas (self):
        for p in self.personas:
            print(p)

    def guardarpersonasenficheroexterno (self):
        listadepersona=open("ficheroext", "wb")
        pickle.dump (self.personas, listadepersona)
        listadepersona.close()
        del (listadepersona)

    def mostarinfoficheroexterno (self):
        print ("La informacion del fichero esterno es la siguiente: ")
        for p in self.personas:
            print (p)

milista=Listapersonas()
persona=Persona("Sandra", "Femenino", 28)
milista.agregarPersonas(persona)
milista.mostarinfoficheroexterno ()