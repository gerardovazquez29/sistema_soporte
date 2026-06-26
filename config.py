# Configuracion general del sistema
import os
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

# Asignamos las constantes
APP_NOMBRE = "Sistema de soporte Tecnico"
APP_VERSION = "1.0"

# Credenciales de la Base de datos (Seguras)
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT", "5432")



ADMIN_USER = "admin"
ADMIN_CLAVE = "1234"
MAX_INTENTOS = 3

#print("HOST :", repr(DB_HOST))
#print("DB   :", repr(DB_NAME))
#print("USER :", repr(DB_USER))
#print("PASS :", repr(DB_PASS))
#print("PORT :", repr(DB_PORT))
