#.Programa que calcule dos operandos con los 7 operadores vistos en clase. Como puedes forzar que el resultado de la division tenga 2 decimales?
operando1 = float(input("Introduce el primer operando: "))
operando2 = float(input("Introduce el segundo operando: "))

suma = operando1 + operando2
resta = operando1 - operando2
multiplicacion = operando1 * operando2
division = operando1 / operando2
potencia = operando1 ** operando2
division_entera = operando1 // operando2
modulo = operando1 % operando2

print(f"La suma es: {suma:.0f}")
print(f"La resta es: {resta:.0f}")
print(f"La multiplicacion es: {multiplicacion:.0f}")
print(f"La division es: {division:.2f}")
print(f"La potencia es: {potencia:.0f}")
print(f"La division entera es: {division_entera:.0f}")
print(f"El modulo es: {modulo:.0f}")