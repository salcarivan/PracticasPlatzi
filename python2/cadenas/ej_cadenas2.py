email=input("Introduce tu email: ")
arroba=email.count("@")
if (arroba!=1 or email.find("@")==0 or email.rfind("@")==(len(email)-1)):
    print ("Email incorrecto")
else:
    print ("Email correcto")
print ((len(email)-1))
