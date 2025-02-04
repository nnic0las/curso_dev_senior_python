from abc import ABC, abstractmethod

class Sujeto:
    
    def __init__(self):
        self._observadores = []

    def agregar_observador(self, observador):
        self._observadores.append(observador)

    def quitar_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observador(Self, mensaje):
        for observador in Self._observadores:
            observador.actualizar(mensaje)

class Observador(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def actualizar(self, mensaje):
        #gestion de errores
        raise NotImplementedError("subclases deben estar implementadas")
    
class ObservadorConcreto(Observador):

    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"{self.nombre} reciobio: {mensaje}")


sujeto = Sujeto()

obs1 = ObservadorConcreto("observador 1")
obs2 = ObservadorConcreto("observador 2")

sujeto.agregar_observador(obs1)
sujeto.agregar_observador(obs2)

sujeto.notificar_observador("mensaje de advertencia LPTx")

