import ejercicio032
numeros = []
for a in range(0,10):
    obtenido = input(f"Introduce el numero {a+1} de 10: ")
    numeros.append(int(obtenido))

cuadrados = ejercicio032.calcular_cuadrados(numeros)
print(cuadrados)
