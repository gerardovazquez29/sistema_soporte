# Este archivo contendra los moldes (clases) de nuestro sistema
# clase usuario
from database import conectar_db
from logs import registrar_eventos
from typing import Optional
from errores import NombreInvalidoError, RolInvalidoError


class Usuario:
    ROLES_PERMITIDOS = ["admin", "tecnico", "viewer"]
    
    def __init__(self,id: Optional[int], nombre: str, rol: str, activo: bool = True):
        self.id = id
        self.nombre = nombre
        self.rol = rol
        self.activo = activo
        
    @property    
    def nombre(self):
         return self._nombre
     
    @nombre.setter
    def nombre(self, valor):
        if len(valor.strip()) < 3:
            raise NombreInvalidoError("El nombre debe tener al menos 3 caracteres.")
        self._nombre = valor.strip()
    
    @property
    def rol(self):
        return self._rol
    
    @rol.setter
    def rol(self, valor):
        if valor.lower() not in self.ROLES_PERMITIDOS:
            raise RolInvalidoError(f"El rol '{valor}' no existe. Debe ser uno de: {self.ROLES_PERMITIDOS}")
        self._rol = valor.lower()
    
    def mostrar(self):
        estado = "Activo" if self.activo else "Inactivo"
        print(f" [{self.id}] {self.nombre} | Rol: {self.rol} | {estado}")
        
    def desactivar(self):
        self.activo = False
        print(f" Usuario '{self.nombre}' desactivado.")
        
    def cambiar_rol(self, nuevo_rol: str):
        self.rol = nuevo_rol
        print(f" Rol de '{self.nombre}' cambiado a '{nuevo_rol}'.")
        
    def reactivar(self):
        self.activo = True
        print(f" Usuario '{self.nombre}' Reactivado")
    
    def __str__(self):
        return f"Usuario({self.nombre}, {self.rol}, {'Activo' if self.activo else 'Inactivo'})"

    
    def guardar(self):
        if self.id is None:
            self._insertar()
        else:
            self._actualizar()
            
    def _insertar(self):
        conn = conectar_db()
        if conn:
            try:
                cursor = conn.cursor()
                query = """
                        INSERT INTO usuarios (nombre, rol, activo)
                        VALUES (%s, %s, %s)
                        RETURNING id;
                """
                # RETURNING id le dice a PostgreSQL que nos devuelva
                # el id que generó automáticamente para el nuevo registro
                cursor.execute(query, (self.nombre, self.rol, self.activo))
                resultado = cursor.fetchone()
                if resultado is None:
                    print(" No se recibió el id generado al insertar el usuario.")
                    conn.rollback()
                    return
                self.id = resultado[0]
                conn.commit()
                print(f" Usuario '{self.nombre}' guardado con ID {self.id}.")
                registrar_eventos(f"INSERT usuario: {self.nombre} | rol: {self.rol}")
            except Exception as e:
                print(f" Error al insertar: {e}")
                conn.rollback()
            finally:
                cursor.close()
                conn.close()
                
    def _actualizar(self):
        conn = conectar_db()
        if conn:
            try:
                cursor = conn.cursor()
                query = """
                    UPDATE usuarios
                    SET nombre = %s, rol = %s, activo = %s
                    WHERE id = %s
                """
                cursor.execute(query,(self.nombre, self.rol, self.activo, self.id))
                conn.commit()
                print(f" Usuario '{self.nombre}' actualizado en DB.")
                registrar_eventos(f"UPDATE usuario ID {self.id}: {self.nombre} | {self.rol}")
            except Exception as e:
                print(f"Error al actualizar: {e}")
                conn.rollback()
            finally:
                cursor.close()
                conn.close()
                
class Ticket:
    def __init__(self, id, asunto: str, descripcion: str, creado_por: Usuario):
        self.id = id
        self.asunto = asunto
        self.descripcion = descripcion
        self.creado_por = creado_por
        self.estado = "Abierto"
        
    def mostrar_ticket(self):
        print(f"\n[Ticket #{self.id}] - {self.asunto}")
        print(f"Estado: {self.estado}")
        print(f"Reportado por: {self.creado_por.nombre} (Rol: {self.creado_por.rol})")
        print(f"Descripcion: {self.descripcion}")
        
            