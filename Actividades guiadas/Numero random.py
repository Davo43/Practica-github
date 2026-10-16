import random
var_random=random.randint(1,5)
var_usario=int(input("introduce un numero del 1 al 5: "))
if var_usario!=var_random:
    print("fallaste")
else:
    print("acertaste")
if var_usario>5:
    print("El numero insertado es demasiado grande")