contador=0
miemail=input("introduce tu dirección de email: ")
for i in miemail:
    if(i=="@"or i=="."):
       contador=contador+1
if contador==2:
    print("email correcto")
else:
    print("email incorrecto")