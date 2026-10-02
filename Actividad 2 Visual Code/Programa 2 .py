#Programa que introduzca por teclado tres tipos de variables y se muestren por pantalla en el siguiente orden: numero entero, texto y numero decimal.
numero_entero = int(input("Introduce un numero entero: "))
texto = input("Introduce un texto: ")
numero_decimal = float(input("Introduce un numero decimal: "))

print(f"El valor introducido es un {numero_entero}")
print(f"El valor introducido es la letra {texto}")
print(f"El valor introducido es el numero decimal {numero_decimal}")
