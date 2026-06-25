# funciones de apoyo reutilizables

from config import APP_NOMBRE, APP_VERSION

def mostrar_encabezado():
    print("="*50)
    print(f" {APP_NOMBRE} v{APP_VERSION}")
    print("="*50)
    
    
def mostrar_menu(opciones: list):
    for i, opcion in enumerate(opciones, start=1):
        print(f" {i}. {opcion}")
    print("="*50)
    
    
