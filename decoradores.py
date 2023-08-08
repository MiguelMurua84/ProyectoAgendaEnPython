def ingreso_de_nuevo_registro(funcion):
    def envoltura(*args, **kwargs):
        print("Ingreso de nuevo registro - Decorador")
        return funcion(*args, **kwargs)
    return envoltura

def actualizacion_de_registro(funcion):
    def envoltura(*args, **kwargs):
        print("Actualización de registro - Decorador")
        return funcion(*args, **kwargs)
    return envoltura

def eliminacion_de_registro(funcion):
    def envoltura(*args, **kwargs):
        print("Eliminación de registro - Decorador")
        return funcion(*args, **kwargs)
    return envoltura