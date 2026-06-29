from modelos import Usuario

# creamos objetos 
u1 = Usuario(1, "Santiago", "admin")
u2 = Usuario(2, "Gerardo", "admin")
u3 = Usuario(3, "Invitado", "viewer", activo=False)


# usamos metodos
print("=== Lista de usuarios ===")
u1.mostrar()
u2.mostrar()
u3.mostrar()

print("\n=== Desactivando a Gerardo ===")
u2.desactivar()
u2.mostrar()

print("\n=== Cambiando Rol de Santiago ===")
u1.cambiar_rol("superadmin")
u1.mostrar()

print("\n=== Reactivando a Gerardo ===")
u2.reactivar()
u2.mostrar()

print("\n=== Usando __str__ ===")
print(u1)
print(u2)
print(u3)
