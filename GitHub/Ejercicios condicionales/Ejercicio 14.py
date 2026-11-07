#Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas
frase = "A quién madruga Dios ayuda."
palabra = input("Introduce una palabra: ")
if palabra.lower() in frase.lower():
    print("La palabra se encuentra en la posición:", frase.lower().index(palabra.lower()))
else:
    print("La palabra no se encuentra en la frase.")