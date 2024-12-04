'''
Escribe un programa que pida al usuario su edad, salario mensual y número de años de antiguedad
en su empleo. Para ser elegible para un prestamo, debe cumplir con las siguientes condiciones:

- Tener entre 25 y 60 años.
- Tener un salario mensual mayor a $30,000.
- Tener al menos 2 años de antiguedad en su empleo.
si cumple con estas condiciones, imprime "prestamo aprobado".
si no las cumple, indica especificamente cuál o cuales de las condiciones no se cumplen
(por ejemplo, "Edad fuera de rango" o "Antiguedad insuficiente")

'''

edad = int(input("Ingresa tu edad:"))
salario_mensual = int(input("Ingresa tu salario:"))
años_antiguedad = int(input("Ingresa los años de antiguedad:"))


if edad >= 25 and edad <= 60:
    if salario_mensual >= 30000:
        if años_antiguedad >= 2:
            print("Prestamo Aprobado")
        else:
            ("No cumple con la antiguedad")
    else:
        print("Salario insuficiente")
else:
    if edad >= 25 and edad <= 60:
        print("Edad no aplica")
    else:
        print("No cumple ninguna de las anteriores")
        
