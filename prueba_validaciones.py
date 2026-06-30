from modelos import Usuario

print("=== PRUEBA DE VALIDACIONES (SEGURIDAD) ===\n")

try:
    print("Intentando crear usuario con nombre vacio...")
    u1 = Usuario(None, " ", "admin")
except ValueError as e:
    print(f"Atrapamos el error: {e}")

try:
    print("\nIntentando crear usuario con rol de 'gerente'...")
    u2 = Usuario(None, "Santiago", "gerente")
except ValueError as e:
    print(f"Atrapamos el error: {e}")
    
try:
    print("\nIntentendo crear un usuario CORRECTO...")
    u3 = Usuario(None, "Santiago", "ADMIN")
    print(f"Usuario creado: {u3.nombre} con rol {u3.rol}")
except ValueError as e:
    print(f"Error inesperado: {e}")
    
