def crearEstudiantesXML():
    contenidoXML = '<?xml version="1.0" encoding="UTF-8"?>\n'
    contenidoXML += '<students>\n'
    
    for i in range(1, 6):
        contenidoXML += f'  <student id="{i}">\n'
        contenidoXML += f'    <name>nombre{i}</name>\n'
        contenidoXML += f'    <surname>Apellido{i}</surname>\n'
        contenidoXML += f'    <email>email{i}@iticbcn.cat</email>\n'
        contenidoXML += f'    <dni>DNI{i}</dni>\n'
        contenidoXML += '  </student>\n'
    
    contenidoXML += '</students>'

    # Escribir el contenido en un archivo
    with open("students.xml", "w", encoding="utf-8") as f:
        f.write(contenidoXML)
    
    # Mostrar el contenido del archivo por consola
    print(contenidoXML)

# Llamar a la función para crear y mostrar el XML
crearEstudiantesXML()
