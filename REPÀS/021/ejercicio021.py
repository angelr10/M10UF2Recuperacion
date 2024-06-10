
a = input("Introduce 10 números separados por espacios: ")
b = a.split()
listadoNumeros = []

for numero in b:
    listadoNumeros.append(int(numero))

sumaTotal = sum(listadoNumeros)
mediana = sumaTotal / len(listadoNumeros)

listadoNumeros.append(sumaTotal)
listadoNumeros.append(mediana)

print("Suma total:", sumaTotal)
print("mediana:", mediana)
print("Llista completa:", listadoNumeros)
