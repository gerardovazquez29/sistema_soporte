# modulos de gestion de usuarios
from database import conectar_db
from config import ADMIN_USER, ADMIN_CLAVE, MAX_INTENTOS
from logs import registrar_eventos


# conectar con postgresql
def listar_usuarios_db():
    conn = conectar_db()
    if conn:
        cursor = conn.cursor() # el cursor es nuestro puntero en la DB
        cursor.execute("SELECT id, nombre, rol, activo FROM usuarios;")
        usuarios = cursor.fetchall() # traemos todas las filas
        
        print("\n=== USUARIOS DESDE POSTGRESQL ===")
        for u in usuarios:
            # En SQL, los resultados vienen como Tuplas 
            estado = "Activo" if u[3] else "Inactivo"
            print(f" [{u[0]}] {u[1]} | Rol: {u[2]} | {estado}")
        cursor.close()
        conn.close()


def registrar_usuario_db(nombre: str, rol: str):
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()
            # se usa %s para evitar inyecciones SQL (Seguridad Profecional)
            query = "INSERT INTO usuarios (nombre, rol) VAlUES (%s, %s);"
            cursor.execute(query, (nombre, rol))
            
            # Nota sin commit los cambios se pierden al cerrrar la conexion
            conn.commit()
            
            print(f"Usuario '{nombre}' registrado exitosamente en la base de datos.")
            registrar_eventos(f"Registro de usurio DB: {nombre} con el rol {rol}")
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            conn.rollback() # si algo falla deshacemos el intento de cambio
        finally:
            cursor.close()
            conn.close()


def actualizar_rol_usuario_db(nombre: str, nuevo_rol: str):
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()
            # ojo WEB SEARCH: EL WHERE es vital aqui.
            query = "UPDATE usuarios SET rol = %s WHERE nombre = %s;"
            cursor.execute(query, (nuevo_rol, nombre))
            
            conn.commit()
            
            # verificamos si realmente se actualizo algo
            if cursor.rowcount > 0:
                print(f"Rol de '{nombre}' actualizado a '{nuevo_rol}',")
                registrar_eventos(f"Update usuario: {nombre} ahora es {nuevo_rol}")
            else:
                print(f"No se encontro al usuario '{nombre}',")
                
        except Exception as e:
            print(f" Error al actualizar: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
            
         

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

