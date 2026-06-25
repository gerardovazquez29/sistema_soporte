from utilidades import mostrar_encabezado, mostrar_menu
from usuarios import listar_usuarios, login


# Mostramos el encabezado
mostrar_encabezado()

# simulamos un login
login("admin", "1234")

# Mostramos usuarios
listar_usuarios()

# Mostramos el menu
opciones = [
    "Gestionar usuarios",
    "Ver tickets",
    "Inventario de equipos",
    "Salir"
]

mostrar_menu(opciones)




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
