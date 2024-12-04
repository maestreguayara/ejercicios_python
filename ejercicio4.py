'''
Realiza un programa que reciba un año e indique si es un año bisiesto o no 
(un año bisiesto es divisible por 4 pero no por 100, a menos que sea divisible por 400)
'''

año = int(input("Ingresa un año:"))

if ((año % 4 == 0) and not(año % 100 == 0) or (año % 400 == 0)):
    print(año, "Es año bisiesto")

else:
    print(año, " El año no es bisiesto")
    