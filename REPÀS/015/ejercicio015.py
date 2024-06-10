b = []
while True:
    a = int(input("Introduce un numero(0 para finalizar)"))
    if a == 0:
        print("Finalizando recolectacion de numeros...")
        break
    b.append(a)
numerosOrdenados = sorted(b)
c = tuple(numerosOrdenados)
print(c)