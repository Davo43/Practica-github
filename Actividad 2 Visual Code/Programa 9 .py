#Programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
segundos = int(input("Introduce el numero de segundos: "))
minutos = segundos / 60
horas = minutos / 60
print(f"En {segundos} segundos hay {minutos:.2f} minutos y {horas:.2f} horas.")
