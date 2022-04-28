from socket import ALG_OP_SIGN


milista=["Ivan",23,3,1997,"sabado"]
mitupla=tuple(milista)
print(len(mitupla))
mitupla2=("Domingo",)
print(len(mitupla2))
mitupla3= "Voinich", 13,1,1995
print(mitupla3)
mitupla4=("Hector",14,5,2015)
nombre,dia,mes,agno=mitupla4
print(nombre)
print(agno)