salario_presidente=int(input("Intoduce salario presidente: "))
print("salario presidente:"+ str(salario_presidente))

salario_director=int(input("Intoduce salario director: "))
print("salario director:"+ str(salario_director))

salario_jefe_area=int(input("Intoduce salario jefe área: "))
print("salario jefe área:"+ str(salario_jefe_area))

salario_administrativo=int(input("Intoduce salario administrativo: "))
print("salario administrativo:"+ str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona bien")
else:
    print("Algo falla en esta empresa")