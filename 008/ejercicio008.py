a = input("introduce de 1 a 3 palabras")
b = a.split(" ")
c = ""
for d in b:
    primera = d[0]
    ultima = d[-1]
    c += primera+ultima+" "
print("las palabras son: ",c)