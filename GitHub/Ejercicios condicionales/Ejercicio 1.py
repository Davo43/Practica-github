#Programa que introduzca dos numeros y devuelva cual de los dos es mayor, menor o son iguales
numero1 = int(input("Introduce el primer número entero: "))
numero2 = int(input("Introduce el segundo número entero: "))
if numero1 > numero2:
    print("El número", numero1, "es mayor que el número", numero2)
elif numero1 < numero2:
    print("El número", numero1, "es menor que el número", numero2)
else:
    print("Los dos números son iguales.")