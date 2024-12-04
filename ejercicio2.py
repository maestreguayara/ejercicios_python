'''
Pide al usurio la hora de entrada y la hora de salida de un estacionamiento.
Si el tiempo de estancia es menor a 2 horas, la tarifa es gratis; entre 2 y 5 horas, la tarifa 
es de $10 por hora; más de 5 horas, la tarifa es de $15 por hora.
Usa condicionales y operadores lógicos para calcular la tarifa total.

''' 

horas = int(input("Ingresa la cantidad de horas que te quedaste:"))

monto_final = 0 
if horas >= 2 and horas <= 5:
    monto_final == horas * 10
    print("Tu ratrifa es", horas * 10)
elif horas > 5:
    monto_final == horas * 15
    print("Tu tarifa es", horas * 15)
else:
    print("es gratis")