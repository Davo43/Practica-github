#Programa que pida cinco palabras y muestre una frase con las cinco. Modifica el codigo para que entre palabra y palabra haya una coma.
palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")
palabra3 = input("Introduce la tercera palabra: ")
palabra4 = input("Introduce la cuarta palabra: ")
palabra5 = input("Introduce la quinta palabra: ")
frase_sin_comas = palabra1 + palabra2 + palabra3 + palabra4 + palabra5
frase_con_comas = palabra1 + "," + palabra2 + "," + palabra3 + "," + palabra4 + "," + palabra5
print(f"La frase sin comas formada es: {frase_sin_comas}")
print(f"La frase con comas formada es: {frase_con_comas}")