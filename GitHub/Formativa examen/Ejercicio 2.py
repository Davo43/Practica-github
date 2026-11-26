#Ejercicio 2

codigo=input("Introduce el codigo del producto: ")
codigo=codigo.strip()
print(codigo)
mayus=codigo.upper()
print(mayus)
minus=codigo.lower()
print(minus)
digitos=len(codigo)
print("Caracteres: ", digitos)
guion=codigo.count("-")
print("Guiones: ", guion)
if "tec" in minus:
    print("Tec: sí")
else:
    print("Tec: no")
if codigo.endswith ("25"):
    print("Colección 25: sí")
else:
    print("Colección 25: no")