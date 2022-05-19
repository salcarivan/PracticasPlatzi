from io import open
archtxt=open("archivo.txt","r+")#lectura y escritura

archtxt.write("Comienzo del texto")

listatxt=archtxt.readlines()

listatxt[1]="Esta linea ha sida incluida desde el exterior\n"

archtxt.seek(0)

archtxt.writelines(listatxt)

archtxt.close()