from modelos import Usuario
from errores import NombreInvalidoError, RolInvalidoError

print("=== PRUEBA DE VALIDACIONES (SEGURIDAD) ===\n")

try:
    print("Intentando crear usuario con nombre vacio...")
    u1 = Usuario(None, " ", "admin")
except NombreInvalidoError as e:
    print(f"Atrapamos el error: {e}")

try:
    print("\nIntentando crear usuario con rol de 'gerente'...")
    u2 = Usuario(None, "Santiago", "gerente")
except RolInvalidoError as e:
    print(f"Atrapamos el error: {e}")
    
try:
    print("\nIntentendo crear un usuario CORRECTO...")
    u3 = Usuario(None, "Santiago", "ADMIN")
    print(f"Usuario creado: {u3.nombre} con rol {u3.rol}")
except NombreInvalidoError as e:
    print(f"Error inesperado: {e}")
    
