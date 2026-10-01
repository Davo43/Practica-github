#Programa que introduzca por teclado tres tipos de variables y se muestren por pantalla en el siguiente orden: número entero, texto y número decimal.
numero_entero = int(input("Introduce un número entero: "))
texto = input("Introduce un texto: ")
numero_decimal = float(input("Introduce un número decimal: "))

print(f"El valor introducido es un {numero_entero}")
print(f"El valor introducido es la letra {texto}")
print(f"El valor introducido es el número decimal {numero_decimal}")
