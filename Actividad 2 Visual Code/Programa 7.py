#.Programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?
operando1 = float(input("Introduce el primer operando: "))
operando2 = float(input("Introduce el segundo operando: "))

suma = operando1 + operando2
resta = operando1 - operando2
multiplicacion = operando1 * operando2
division = operando1 / operando2
exponente = operando1 ** operando2
division_entera = operando1 // operando2
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicación es: {multiplicacion}")
print(f"La división es: {division:.2f}")
print(f"El exponente es: {exponente}")
print(f"La división entera es: {division_entera:.0f}")
