import math
def calculaRaiz(num1):
    if num1<=0:
        raise ValueError ("El numero no puede ser 0 o negativo")
    else:
        return math.sqrt(num1)
op1=(int(input("Introduce un número. ")))
try:
    print(calculaRaiz(op1))
except ValueError as ErrordeNumeroNegativo:
    print(ErrordeNumeroNegativo)
print("Programa terminado")