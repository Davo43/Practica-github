#Programa que calcula una ecuacion de segundo grado. Controla que el valor de la raiz cuadrada no de un valor negativo
import math
numero1 = int(input("Introduce el numero 1 (a)"))
numero2 = int(input("Introduce el numero 2 (b)"))
numero3 = int(input("Introduce el numero 3 (c)"))
raiz = numero2**2-4*numero1*numero3
if raiz < 0:
    print("La ecuacion no tiene solucion real")
elif raiz == 0:
    x = -numero2/(2*numero1)
    print(f"La ecuacion tiene una solucion real: {x}")
else:
    x1 = (-numero2 + math.sqrt(raiz)) / (2 * numero1)
    x2 = (-numero2 - math.sqrt(raiz)) / (2 * numero1)
    print(f"La ecuacion tiene dos soluciones reales: {x1} y {x2}")