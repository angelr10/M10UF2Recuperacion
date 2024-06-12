#Archivo encargado de contener metodos encargados de actualizar informacion en la tabla
def actualizarInformacion(cursor):
    cursor.execute("UPDATE vehiculo SET precio = 10000 WHERE id = 1;")