# Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif
letra = input("Introduce una letra: ")
if letra.isupper():
    mayuscula = True
if letra.islower():
    mayuscula = False
if letra.isdigit():
    numero = True
if letra.isupper():
    print("La letra está en mayúscula")
elif letra.islower():
    print("La letra está en minúscula")
elif letra.isdigit():
    print("El valor introducido es un número")
else:
    print("El valor introducido es un símbolo")