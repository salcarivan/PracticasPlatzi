from io import open
archtxt=open("archivo.txt","r")

#texto=archtxt.read()
texto=archtxt.readlines()

archtxt.close()

print(texto[-1])