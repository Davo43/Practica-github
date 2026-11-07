#Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.
frase = "A quién madruga Dios ayuda."
palabra = input("Introduce una palabra: ")
if palabra in frase:
    print("La palabra se encuentra en la posición:", frase.index(palabra))
else:
    print("La palabra no se encuentra en la frase.")