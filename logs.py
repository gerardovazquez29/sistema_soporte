import datetime

def registrar_eventos(mensaje: str):
    # la opcion "a" es de 'append' (agregar al final)
    with open("eventos.txt", "a") as archivo:
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"[{fecha_hora}] {mensaje}\n")
    print("LOG: Evento registrado en el archivo.")
    
    
def registrar_error(error_desc: str):
    registrar_eventos(f"CRITICAL_ERROR | {error_desc}")
    
