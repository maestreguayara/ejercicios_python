''' 
Pide al usuario que ingrese su edad y determina si es un niño (0-12), 
adolescente (13-17), adulto (18-64) o adulto mayor (65+)
''' 

edad = int(input("Ingresa tu edad:"))

if edad <= 12:
    print("Eres un niñ@")  
elif edad >= 13 and edad <= 17:
    print("Eres un adolescente")
elif edad >= 18 and edad <= 64:
    print("Eres un adulto")
else:
    print("eres un anciano")