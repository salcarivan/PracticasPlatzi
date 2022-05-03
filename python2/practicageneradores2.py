def devuelveciudades (*ciudades):
    for elemento in ciudades:
        #for subelemento in elemento:
            yield from elemento
ciudadesdevueltas=devuelveciudades("Madrid","Sevilla","Cádiz","Málaga","Huelva","Córdoba","Almería","Jaen","Granada","Barcelona", "Santiago","Londres","Roma")
print(next(ciudadesdevueltas))
print(next(ciudadesdevueltas))
