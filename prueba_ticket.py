from modelos import Usuario, Ticket

# 1. Creamos al usuario (El autor)
autor = Usuario(1, "Santiago", "admin")


# 2. Creamos el ticket y le pasamos el OBJETO autor
ticket1 = Ticket(101, "Error de red", "la VM de Ubuntu no tiene internet", autor)


# 3. Mostramos la información
ticket1.mostrar_ticket()
