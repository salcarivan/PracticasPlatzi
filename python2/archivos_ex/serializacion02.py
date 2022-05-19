import pickle

fichero=open("lstnom", "rb")

lista=pickle.load(fichero)

print(lista)