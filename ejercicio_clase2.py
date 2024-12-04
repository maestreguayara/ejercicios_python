# pedir año de nacimiento y año actual 
# imprimir su edad 

print("Ingresa tu año de nacimiento y el año actual")
año_n = int(input("año-n: "))
año_a = int(input("año-a: "))
edad = año_a - año_n

print("En este año {} tienes {} años ".format(año_a,edad))
