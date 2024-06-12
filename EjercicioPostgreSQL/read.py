#Archivo encargado de contener metodos de lectura de informacion en la tabla
def mostrarTabla(cursor):
    cursor.execute("SELECT * from vehiculo;")
    contenido = cursor.fetchall()
    return contenido