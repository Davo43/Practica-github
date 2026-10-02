#Realiza un programa que a partir de introducir el diametro de un circulo calcule el area y perimetro. Importa la libreria match y utiliza el valor PI para hacer el calculo. Redondea el resultado a un decimal.
import math
diametro = float(input("Introduce el valor del diametro del circulo: "))
area = math.pi * (diametro / 2) ** 2
perimetro = math.pi * diametro
print(f"El perimetro del circulo es: {perimetro:.1f}")
print(f"El area del circulo es: {area:.1f}")
