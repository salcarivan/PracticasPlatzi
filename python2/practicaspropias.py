def calnump (nump1):
    while nump1<=0:
        raise ValueError ("El numero no puede ser 0 o negativo")
    else:
        div=nump1%2
        if div==0:
            print ("No es primo")
        elif div!=0:
            print ("Es primo")
        elif nump1==1:
            print ("Es primo")
        
nump1=(int(input("Introduce un número entero: ")))
try:
    print (calnump(nump1))
except ValueError as ErrorNumeronegativo:
    nump1=(int(input("Introduce un número entero: ")))
