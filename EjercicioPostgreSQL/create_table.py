import connection
import psycopg2
from psycopg2 import sql
#Arhivo encargado de la creacion de la tabla

def crearTabla(cursor):
    try:
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS vehiculo (
                    id SERIAL PRIMARY KEY,
                    marca VARCHAR(50) NOT NULL,
                    modelo VARCHAR(50) NOT NULL,
                    ano INTEGER NOT NULL,
                    precio DECIMAL(10, 2) NOT NULL,
                    color VARCHAR(20)
                );
            """)
        print("Tabla creada con exito!!!")
    except Exception as error:
        print("Error al crear la tabla:", error)