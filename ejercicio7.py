# escribe un programa que sume todos lo números que hay 
# en un determinado rango. 
# el programa pregunta al usurio el inicio y el fin.

suma_rango = 0 

inicio = int(input("ingresa el numero inicial:"))
final = int(input("ingresa el numero final:"))


for i in range(inicio, final+1,1):
    suma_rango += i 

print(f"la suma total de {inicio} y {final} es: {suma_rango}")