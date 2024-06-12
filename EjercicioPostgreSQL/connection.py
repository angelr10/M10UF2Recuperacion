import psycopg2
from psycopg2 import sql
#Archivo encargado de gestionar la conexion e informacion a la bdd y a la tabla
#Contraseña : angel1
#Puerto : 8585
def establecerConexion():
    opcionbdd = input("Quieres meter a mano la informacion de la bdd?")
    if(opcionbdd == "si" or opcionbdd=="s"):
        nombrebdd = input("Introduce el nombre de la bdd:")
        usuario = input("Introduce el usuario:")
        contra = input("Introduce el contra:")
        host = input("Introduce el host:")
        puerto = input("Introduce el puerto:")
    else:
        nombrebdd = "postgres"
        usuario = "postgres"
        contra = "angel1"
        host = "localhost"
        puerto = "8585"
    try:
        connection = psycopg2.connect(
            dbname=nombrebdd,
            user=usuario,
            password=contra,
            host=host,
            port=puerto
        )
        cursor = connection.cursor()
        print("Conexion exitosa a la base de datos!")
        return connection,cursor
    except(Exception, psycopg2.Error):
        print("Has tenido un problema con las especificaciones de la base de datos, intentalo de nuevo.")
    
