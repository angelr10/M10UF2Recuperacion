# Solicitar entrada al usuario
a = input("Introduce dos palabras separadas por un espacio: ")

# Dividir la cadena en una lista de palabras
b = a.split(" ")

palabra1 = b[1][:2] + b[0][2:]
palabra2 = b[0][:2] + b[1][2:]

print("Palbaras resultado : ",palabra1,palabra2)
