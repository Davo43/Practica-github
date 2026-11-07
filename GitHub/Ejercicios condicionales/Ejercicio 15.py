#Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años
frase = "No hay mal que dure cien años"
a = 0
e = 0
i = 0
o = 0
u = 0
for letra in frase.lower():
    if letra == "a":
        a += 1
    elif letra == "e":
        e += 1
    elif letra == "i":
        i += 1
    elif letra == "o":
        o += 1
    elif letra == "u":
        u += 1
print("Número de a:", a, "Número de e:", e, "Número de i:", i, "Número de o:", o, "Número de u:", u)
