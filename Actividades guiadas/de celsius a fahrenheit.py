grados=float(input("Introduce los grados: "))
#F=c*9/5+32

calculo=grados * 5/9 +32
print("Temperatura:" ,calculo, "ºF")

#otra manera de presentar la infromacion con print

#print(f"2ª manera de presentar Temperatura: {calculo} ºF")
#primer metodo de redondeo
print(round(calculo,2))
print(f"temperatura: {calculo:.2f} ºF")
