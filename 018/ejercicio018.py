a = input("Introduce dos palabras: ")
letrasEncontradas = ""

# Encontrar todas las letras únicas, excluyendo espacios
for b in a:
    if b not in letrasEncontradas and b != " ":
        letrasEncontradas += b

# Crear una lista para almacenar las letras únicas y su conteo
contadores = []
for letra in letrasEncontradas:
    contador = a.count(letra)
    contadores.append((letra, contador))

contadorTupla = tuple(contadores)
print(contadorTupla)
