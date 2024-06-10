a = input("Introudce 10 numeros separados por un espacio: ")
b = a.split(" ")
numerosAINT = [int(num) for num in b]
numerosOrdenados = sorted(numerosAINT)
tuplaOrdenada = tuple(numerosOrdenados)
print(tuplaOrdenada)