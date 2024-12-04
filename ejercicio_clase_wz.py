telefono = input("ingresa tu numero de telefono:")

if len(telefono) == 10 and (telefono[0] in ["6", "7", "8", "9"]) and telefono.isdigit():
    print("El numero de telefono es valido.")
else:
    print("El numero de telefono no es valido.")