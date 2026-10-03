"""Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el 
peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado 
es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso"""
peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))
imc = peso / (estatura ** 2)
print(f"si pesas {peso:.1f} kg y mides {estatura:.2f} m, tu IMC es: {imc:.2f}")
if imc >= 25:
    print("Tienes sobrepeso.")