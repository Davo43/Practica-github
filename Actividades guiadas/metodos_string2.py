respuesta=input("Introduce una letra:")
if  respuesta.isnumeric():
    if respuesta.isupper()==False:
        print("es mayuscula")
    else:
        print("es minuscula")
else:
    print("el valor no es una letra")
