from utilidades import mostrar_encabezado, mostrar_menu, pedir_numero
from usuarios import listar_usuarios, login, listar_usuarios_db, registrar_usuario_db, actualizar_rol_usuario_db
from database import test_conexion


# Mostramos el encabezado
mostrar_encabezado()

# simulamos un login
login("admin", "1234")

# Mostramos usuarios
listar_usuarios_db()

# nos conectamos a PostgreSQL
#test_conexion()

# Mostramos el menu
opciones = [
    "Gestionar usuarios",
    "Actualizar usuarios",
    "Ver tickets",
    "Inventario de equipos",
    "Salir"
]

while True:
    try:
        mostrar_menu(opciones)
        numero = pedir_numero("ingresa una opcion: ")
        if numero == 1:
            print(f"\n--- REGISTRO DE NUEVO USUARIO ---")
            nom = input("Nombre del usuario: ")
            puesto = input("Rol (admin/tecnico/viewer): ")
            registrar_usuario_db(nom, puesto)
            # despues de registrar, mostramos la lista actualiozada
            listar_usuarios_db()
            break
        elif numero == 2:
            print("Actualizacion de usuarios")
            nom = input("Nombre del usuario: ")
            puesto = input("nuevo rol (admin/tecnico/viewer): ")
            actualizar_rol_usuario_db(nom, puesto)
            listar_usuarios_db()
            break
        elif numero == 3:
            print("Bienvenido: Ver tickets")
            break
        elif numero == 4:
            print("Bienvenido: Inventario de equipos")
            break
        elif numero == 5:
            print("hasta pronto")
            break
        else:
            print("Opcion no valida")
    except Exception as e:
        print(f"Error inesperado {e}")
        break

"""
==================================================
 Sistema de soporte Tecnico v1.0
==================================================

 Bienvenido, admin. Acceso concedido.

 Lista de usuarios registrados:
========================================
 [1] Santiago | Rol: admin | Activo
 [2] Gerardo | Rol: tecnico | Activo
 [3] Invitado | Rol: viewer | Inactivo
========================================
 1, Gestionar usuarios
 2, Ver tickets
 3, Inventario de equipos
 4, Salir
==================================================
"""
