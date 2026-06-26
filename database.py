import psycopg2
from config import (
    DB_HOST,
    DB_NAME,
    DB_USER,
    DB_PASS,
    DB_PORT
)

def conectar_db():
    try:
        conexion = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        return conexion
    except Exception as e:
        #print("Tipo:", type(e))
        #print("Representación:", repr(e))
        #print("Mensaje:", e)
        #return None
        print(f"Error al conectar a PostgreSQL: {e}")
        return None
    
def test_conexion():
    conn = conectar_db()
    if conn:
        print("Conexion exitosa a PostgreSQL.")
        conn.close()
    else:
        print("Fallo la conexion")



