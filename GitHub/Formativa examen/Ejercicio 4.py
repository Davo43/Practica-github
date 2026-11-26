#Ejercicio4
# Importar la función para generar números aleatorios
import random

# Generar un número aleatorio entre 1 y 100
numero = random.randint(1, 100)

# Solicitar la edad al visitante
edad = input("Introduce tu edad: ")

# Comprobar si la edad es un número
if edad.isdigit():
    edad = int(edad)
    if edad <1 or edad > 100:
        print("Error: la edad debe estar entre 1 y 100 años.")

    # Comprobar si la edad está entre 1 y 100
    if edad < 1 or edad > 100:
        print("Error: la edad debe estar entre 1 y 100 años.")
    else:
        print("Número obtenido en el sorteo:", numero)

        # Asignar el premio según el número obtenido
        if numero >= 1 and numero <= 10:
            print("Premio especial: entrada gratuita.")
        elif numero >= 11 and numero <= 30:
            print("Premio: descuento del 50%.")
        elif numero >= 31 and numero <= 60:
            print("Premio: descuento del 20%.")
        else:
            print("No has conseguido ningún premio.")
else:
    print("Error: debes introducir un número.")
