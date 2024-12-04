# solicita una palabra y cuenta cuantas vocales tiene
# el programa debe mostrar la cantidad de vocales que tine la cadena 

vocales = ["a", "e", "i", "o", "u"]
contador = 0 
cadena = str(input("ingresa una palabra:"))

for a in range (len(cadena)):
    for b in range(len(vocales)):
        if (cadena[a] == str(vocales[b]).casefold()):
            contador = contador + 1
print(f"la cantidad es: {contador}")
