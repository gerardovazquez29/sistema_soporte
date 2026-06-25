# modulos de gestion de usuarios

from config import ADMIN_USER, ADMIN_CLAVE, MAX_INTENTOS
from logs import registrar_eventos


# Base de Datos temporal (despuews conectarla a postgreSQL)

usuarios_db = [
    {"id": 1, "nombre": "Santiago", "rol": "admin", "activo": True },
    {"id": 2, "nombre": "Gerardo", "rol": "tecnico", "activo": True },
    {"id": 3, "nombre": "Invitado", "rol": "viewer", "activo": False },
]

def listar_usuarios():
    print("\n Lista de usuarios registrados: ")
    print("="*40)
    for u in usuarios_db:
        estado = "Activo" if u["activo"] else "Inactivo"
        print(f" [{u['id']}] {u['nombre']} | Rol: {u['rol']} | {estado}")
    print("="*40)
    
def buscar_usuario(nombre: str):
    for u in usuarios_db:
        if u["nombre"].lower() == nombre.lower():
            return u
    return None

def login(user: str, clave: str) -> bool:
    if user == ADMIN_USER and clave == ADMIN_CLAVE:
        print(f"\n Bienvenido, {user}. Acceso concedido.")
        registrar_eventos("Login exitoso del usuario admin")
        return True
    print("\n Credenciales incorrectas.")
    return False

