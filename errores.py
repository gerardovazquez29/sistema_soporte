# errores.py

class SoporteError(Exception):
    """Clase base para todos los errores de nuestro sistema """
    pass

class RolInvalidoError(SoporteError):
    """ Se lanza cuando el rol no esta en la lista permitida """
    pass

class NombreInvalidoError(SoporteError):
    """ Se lanza cuando el nombre no cumple los requisitos """
    pass
