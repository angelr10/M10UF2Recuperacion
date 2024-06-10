def crear_json_books():
    contenidoEnBruto = [
        {"title": "Libro01", "cover": "Cover04", "year": 2001, "pages": 300},
        {"title": "Libro02", "cover": "Cover03", "year": 2002, "pages": 250},
        {"title": "Libro03", "cover": "Cover02", "year": 2003, "pages": 200},
        {"title": "Libro04", "cover": "Cover01", "year": 2004, "pages": 350}
    ]
    contenidoJson = '[\n'
    for libros in contenidoEnBruto:
        stringLibro = (
            f'  {{\n'
            f'    "libros": {{\n'
            f'      "title": "{libros["title"]}",\n'
            f'      "cover": "{libros["cover"]}",\n'
            f'      "year": {libros["year"]},\n'
            f'      "pages": {libros["pages"]}\n'
            f'    }}\n'
            f'  }},\n'
        )
        contenidoJson += stringLibro
    contenidoJson = contenidoJson.rstrip(',\n') + '\n]'
    print(contenidoJson)

    with open("contenidoEnBruto.json", "w", encoding="utf-8") as f:
        f.write(contenidoJson)
crear_json_books()
