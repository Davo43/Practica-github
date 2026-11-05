"""Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El 
resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un 
resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso
(raíz y división)."""
import math
numero = float(input("Introduce un número: "))
raiz_cuadrada = math.sqrt(numero)
division = int(raiz_cuadrada / 2)
print(f"Raíz cuadrada de {numero:.0f}: {raiz_cuadrada:.0f}")
print(f"La división da: {division:.0f}")
