#Archivo encargado de contener metodos que permitiran eliminar informacion en la tabla
def eliminarTabla(cursor):
    cursor.execute("drop table vehiculo;")
    print("Tabla vehiculos eliminada!!!")