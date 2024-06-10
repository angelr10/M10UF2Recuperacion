def leerJson():
    with open("books.json", "r", encoding="utf-8") as f:
        contenido = f.readlines()
    
    for linea in contenido:
        print(linea)

leerJson()
