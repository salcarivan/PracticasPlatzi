class Persona ():
    def __init__(self, nombre, edad, lugar_residencia):
       self.nombre=nombre
       self.edad=edad
       self.lugar=lugar_residencia

    def descripcion(self): 
        print("Nombre:", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ",self.lugar)

class Empleado(Persona):
    def __init__(self, salario, antigüedad,nom_empleado,edad_empleado,residencia_empleado):
        super().__init__(nom_empleado, edad_empleado, residencia_empleado)
        self.salario=salario
        self.antigüedad=antigüedad
    
    def descripcion (self):
        super().descripcion()
        print ("Salario:", self.salario, "\nAntiguedad: ", self.antigüedad)

Manuel=Persona ("Manuel",55,"Colombia")
Manuel.descripcion()

print(isinstance(Manuel,Empleado))
