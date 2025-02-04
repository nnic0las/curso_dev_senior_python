from abc import ABC, abstractmethod

class Estrategia_Descuento(ABC):

    @abstractmethod
    def calcular(self, monto):
        pass

class Sin_Descuento(Estrategia_Descuento):

    def calcular(self, monto):
        return monto
    
class Descuento_Porcentaje(Estrategia_Descuento):

    def __init__(self, porcentaje):
        self.porcentaje = porcentaje

    def calcular(self, monto):
        return monto - (monto * self.porcentaje / 100)
    
class Descuento_Fijo(Estrategia_Descuento):
    
    def __init__(self, montoDescuento):
        self.montoDescuento = montoDescuento

    def calcular(self, monto):
        return monto - self.montoDescuento
    
class Pedido:

    def __init__(self, monto, estrategiaDescuento: Estrategia_Descuento):
        self.monto = monto
        self.estrategiaDescuento = estrategiaDescuento

    def calcularTotal(self):
        return self.estrategiaDescuento.calcular(self.monto)
    
pedido1 = Pedido(1000,Sin_Descuento())
print(f"Total sin descuento {pedido1.calcularTotal()}")

pedido2 = Pedido(1000, Descuento_Porcentaje(50))
print(f"Total con 50% de descuento {pedido2.calcularTotal()}")

pedido3 = Pedido(1000, Descuento_Fijo(100))
print(f"Total de descuento fijo $100 ${pedido3.calcularTotal()}")



