# prueba_active_record.py
from modelos import Usuario
from usuarios import obtener_objetos_usuarios

print("=== PRUEBA ACTIVE RECORD ===\n")

# ─── PRUEBA 1: Crear usuario nuevo y guardarlo ───
print("--- Creando usuario nuevo ---")
nuevo = Usuario(None, "Carlos", "tecnico")
nuevo.guardar()
print(f"ID asignado por PostgreSQL: {nuevo.id}\n")

# ─── PRUEBA 2: ver todos los usuarios ───
print("--- Usuarios actuales en DB ---")
usuarios = obtener_objetos_usuarios()
for u in usuarios:
    u.mostrar()
    
# ─── PRUEBA 3: Modificar y guardar ───
print("\n--- Desactivando a Carlos ---")
nuevo.desactivar()
nuevo.guardar()

# ─── PRUEBA 4: Estado final ───
print("\n--- Estado final en DB ---")
usuarios_final = obtener_objetos_usuarios()
for u in usuarios_final:
    u.mostrar()
    