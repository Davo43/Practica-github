#Programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
segundos = int(input("Introduce el numero de segundos: "))
minutos = segundos / 60
horas = minutos / 60
print("El numero de minutos es: ", minutos, " y en horas es: ", horas, ".")
