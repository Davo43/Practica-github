#Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isosceles, nos devuelva por pantalla en el area y el perimetro.
lado = float(input("Introduce el valor del lado: "))
base_menor = float(input("Introduce el valor de la base menor: "))
base_mayor = float(input("Introduce el valor de la base mayor: "))
altura = float(input("Introduce el valor de la altura: "))
area = (base_menor + base_mayor) * altura / 2
perimetro = 2 * lado + base_menor + base_mayor
print(f"El area del trapecio es: {area:.1f}")
print(f"El perimetro del trapecio es: {perimetro:.0f}")