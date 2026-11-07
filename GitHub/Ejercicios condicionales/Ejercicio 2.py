#0. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados numeros entre 0 y 10
numero1 = int(input("Introduce el primer número entero (entre 0 y 10): "))
numero2 = int(input("Introduce el segundo número entero (entre 0 y 10): "))

if numero1 < 0 or numero1 > 10:
    print("El numero1 no esta entre el 1 y el 10.")
elif numero2 < 0 or numero2 > 10:
    print("El numero2 no esta entre el 1 y el 10.")
else:
    if numero1 > numero2:
        print("El número", numero1, "es mayor que el número", numero2)
    elif numero1 < numero2:
        print("El número", numero1, "es menor que el número", numero2)
    else:
        print("Los dos números son iguales.")