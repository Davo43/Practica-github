# Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
letra = input("Introduce una letra: ")
if letra.isupper():
    mayuscula = True
if letra.islower():
    mayuscula = False
if letra.islower():
    print("La letra está en minúscula")
elif mayuscula == True:
    print("La letra está en mayúscula")
else:
    print("La letra es mayúscula¿?")