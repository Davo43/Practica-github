# Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla.
letra = input("Introduce una letra: ")
if letra.Isupper():
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
    print("La letra es mayúscula¿?")