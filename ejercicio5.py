# crea un programa que genere y muestre la tabla de multiplicar 
# de un número introducido por el usuario(del 1 al 12)

numero = int(input("ingresa un número:")) 
for i in range (1, 13, 1):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")