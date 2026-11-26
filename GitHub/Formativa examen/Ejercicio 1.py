#Ejercicio 1
import math
x1 = int(input("Introduce la x inicial: "))
y1 = int(input("Introduce la y inicial: "))
x2 = int(input("Introduce la x final: "))
y2 = int(input("Introduce la y final: "))
resultado = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("La distancia es:", round(resultado, 2)," metros")