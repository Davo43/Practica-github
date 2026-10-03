"""Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan 
importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores 
de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por 
teclado el número de menores y el número de adultos que asisten al cine """
precio_entrada = 12
numero_menores = int(input("Introduce el número de menores: "))
numero_adultos = int(input("Introduce el número de adultos: "))
total_menores = numero_menores * precio_entrada * 0.5
total_adultos = numero_adultos * precio_entrada * 0.9
print(f"Precio de menores: {total_menores:.2f} euros")
print(f"Precio de adultos: {total_adultos:.2f} euros")
