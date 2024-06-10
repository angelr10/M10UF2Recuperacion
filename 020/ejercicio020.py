contactos = {}

while True:
    nombre = input("Introduce el nombre: ")
    if nombre=="salir":
        break
    if nombre in contactos:
        print("Este nombre ya existe, por lo tanto no se agregara")
        continue

    edad = input("Introduce la edad: ")
    contactos[nombre] = edad
print("Finalizando... Los resultados son...")
for a,b in contactos.items():
    print(a,b)
