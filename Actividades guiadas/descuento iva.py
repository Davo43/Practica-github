precio = float(input("Introduce el precio del producto: "))
descuento = precio - precio * 10/100
iva = descuento + descuento * 21/100

print("Precio con descuento son", descuento, "€")
print("Precio con IVA son", iva, " €")

iva=precio * (1-10/100) * (1+21/100)
#dos formas de printear
print("Nuevo resultado",round(iva, 2))
print(f"Nuevo resultado {iva:.2f}")
print(f"El producto con precio de {precio}, con el descuento, {descuento}€ y con el IVA, un total de {iva:.2f} €")
