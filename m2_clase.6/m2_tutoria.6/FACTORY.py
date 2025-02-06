from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def create(self):
        pass

class Carro(Vehiculo):
    def create(self):
        return "se creo un carro"
    
class Moto(Vehiculo):
    def create(self):
        return "se creo una moto"
    
class VehiculoFactory:
    @staticmethod
    def get_vehiculo(vehiculo_tipo):
        if vehiculo_tipo == "carro":
            return Carro()
        elif vehiculo_tipo == "moto":
            return Moto()
        else:
            raise ValueError("tipo de vehiculo desconocido")
        
try:
    factory = VehiculoFactory()

    car = factory.get_vehiculo("carro")
    print(car.create())

    motorcycle = factory.get_vehiculo("moto")
    print(motorcycle.create())
except ValueError as e:
    print(e)
