import pickle

lst=["Pedro","Ana", "María", "Isabel"]

fichero_binario=open("lstnom","wb")

pickle.dump(lst,fichero_binario)

fichero_binario.close()

del(fichero_binario)