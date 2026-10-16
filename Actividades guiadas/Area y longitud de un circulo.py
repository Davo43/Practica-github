import math
radio = float(input("Introduce el radio: "))
longitud= 2*radio*math.pi
area= math.pi *radio ** 2
print(longitud)
print(area)
#Primer método redondeo
print(f"La longitud del criculo es: {longitud:.2f}")
print(math.ceil(area))
print("La longitud del criculo es: ",round(longitud,2))
print(math.floor(area))