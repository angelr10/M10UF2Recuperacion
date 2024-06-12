#Archivo encargado de contener metodos de creacion de informacion de contenido de la tabla
def añadirContenido(cursor):
    cursor.execute("""
            INSERT INTO vehiculo (marca, modelo, ano, precio, color)
            VALUES ('zitroen', 'cactus', 2, 20, 'rojo');
        """)