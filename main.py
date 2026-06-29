from utilidades import mostrar_encabezado, mostrar_menu, pedir_numero
from usuarios import login, listar_usuarios_db, menu_gestionar_usuarios, obtener_objetos_usuarios


# Mostramos el encabezado
mostrar_encabezado()

# simulamos un login
login("admin", "1234")

# Mostramos usuarios
listar_usuarios_db()

# nos conectamos a PostgreSQL
#test_conexion()

mis_usuarios = obtener_objetos_usuarios()

for u in mis_usuarios:
    u.mostrar()
    if u.nombre == "Gerardo":
        u.reactivar()

# Mostramos el menu
opciones = [
    "Gestionar usuarios",
    "Ver tickets",
    "Inventario de equipos",
    "Salir"
]

while True:
    try:
        mostrar_menu(opciones)
        numero = pedir_numero("ingresa una opcion: ")
        if numero == 1:
            menu_gestionar_usuarios()
            
        elif numero == 2:
            print("Modulo de tickets ")

        elif numero == 3:
            print("Modulo de inventario")
            
        elif numero == 4:
            print("hasta pronto")
            break
        
        else:
            print("Opcion no valida")
            
    except Exception as e:
        print(f"Error inesperado {e}")
        break

"""

"""
