#Archivo encargado de las llamadas y gestion del orden del resto de tablas
import create_table
import connection
import read
import create
import update
import delete
def main():
    print("iniciando programa...")
    conn, cursor = connection.establecerConexion()
    
    opcion1 = input("Quieres crear la tabla?")
    if(opcion1 == "si" or opcion1 =="s"):
        create_table.crearTabla(cursor)
    opcion2 = input("Quieres añadir contenido a la tabla?")
    if(opcion2 == "si" or opcion2 =="s"):
        create.añadirContenido(cursor)
    opcion3 = input("Quieres leer la tabla?")
    if(opcion3 == "si" or opcion3 =="s"):
        contenido = read.mostrarTabla(cursor)
        for cont in contenido:
            print(cont)
    opcion4 = input("Quieres modificar la tabla?")
    if(opcion4 == "si" or opcion4 =="s"):
        update.actualizarInformacion(cursor)
        contenido2 = read.mostrarTabla(cursor)
        print("Contenido actualizado: ")
        for cont in contenido2:
            print(cont)
    opcion5 = input("Quieres eliminar la tabla?")
    if(opcion5 == "si" or opcion5 =="s"):
        delete.eliminarTabla(cursor)
        

main()
