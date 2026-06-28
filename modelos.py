# Este archivo contendra los moldes (clases) de nuestro sistema
# clase usuario

class Usuario:
    def __init__(self,id: int, nombre: str, rol: str, activo: bool = True):
        self.id = id
        self.nombre = nombre
        self.rol = rol
        self.activo = activo
        
    def mostrar(self):
        estado = "Activo" if self.activo else "Inactivo"
        print(f" [{self.id}] {self.nombre} | Rol: {self.rol} | {estado}")
        
    def desactivar(self):
        self.activo = False
        print(f" Usuario '{self.nombre}' desactivado.")
        
    def cambiar_rol(self, nuevo_rol: str):
        self.rol = nuevo_rol
        print(f" Rol de '{self.nombre}' cambiado a '{nuevo_rol}'.")
        
    def __str__(self):
        return f"Usuario({self.nombre}, {self.rol}, {'Activo' if self.activo else 'Inactivo'})"


