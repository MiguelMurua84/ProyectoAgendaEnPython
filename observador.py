class Sujeto():

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(args)

class Observador():

    def update(self, ):
        raise NotImplementedError("Delegación de actualización")

    def delete(self, ):
        raise NotImplementedError("Delegación de eliminación")
    
class ConcretoObserverA(Observador):
    def __init__(self, obj):
        self.observador_a = obj
        self.observador_a.agregar(self,)

    def update(self, *args):
        print("Actualización dentro de un Observador ConcretoObservadorA")
        print("Parámetros: ", args)

    def delete(self, *args):
        print("Actualización dentro de un Observador ConcretoObservadorA")
        print("Se elimino ID: ", args)



