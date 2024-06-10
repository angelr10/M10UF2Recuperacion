a = input("Introduce una frase: ")
b = a.split(" ")
#Eliminar repetidos letras repetidas de las palabras y las almacenamos
bLimpio = []
for palabra in b:#Lectura de palabras
    caracteresEncontrados = ""
    for letra in palabra:#lectura de caracteres
         if letra not in caracteresEncontrados:
              caracteresEncontrados += letra
    bLimpio.append(caracteresEncontrados)

c = tuple(bLimpio)
print(c)
