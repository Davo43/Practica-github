#Ejercicio3
edad=int(input("Introduce tu edad: "))
conducir=input("Tienes carnet de conducir (s/n): ")
socio=input("Tienes carnet de socio (s/n): ")
mayus_cond=conducir.upper()
mayus_socio=socio.upper()
if edad<18:
    print("No tienes la edad suficiente.")
elif mayus_cond == "N" and mayus_socio =="N":
    print("No cumples los requisitos.")
else:
    print("Puedes alquilar la bici. ")