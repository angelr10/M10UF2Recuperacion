a = int(input("Introduce un numero del 0 al 10: "))
numeros = 10
almacenados = ""
for c in range(1,numeros+1):
    almacenados += str(a*c)+","
almacenados = almacenados.rstrip(',')
print(almacenados)