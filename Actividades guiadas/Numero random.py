import random
var_random=random.randint(1,5)
var_usario=int(input("introduce un numero del 1 al 5: "))
if var_usario in "1,2,3,4,5":

    if int(var_usario)==var_random:
        print("Fallaste")
    else:
        print("Acertaste")
else:
    print("El numero insertado es demasiado grande")