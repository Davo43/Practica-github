#Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif con
#  operadores lógicos.

nota = float(input("Introduce una nota entre 0 y 10: "))

if nota >= 0 and nota <= 10:
	if nota >= 8.5 and nota <= 10:
		print("Excelente")
	elif nota >= 6.5 and nota < 8.5:
		print("Notable")
	elif nota >= 5 and nota < 6.5:
		print("Satisfactorio")
	elif nota >= 0 and nota < 5:
		print("Insuficiente")
else:
	print("La nota debe estar entre 0 y 10")

