precio = float(input("Introduce el precio del producto: "))
descuento = precio * 0.10
precio_con_descuento = precio - descuento
iva = precio_con_descuento * 0.21
precio_con_iva = iva + precio_con_descuento
print(f"El precio total es {iva:.2f} €")
