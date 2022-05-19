from io import open

archtxt=open("archivo.txt","w")

frase="Hoy miercoles stengo que llamar a mi hermano\n Miguel"

archtxt.write(frase)

archtxt.close()