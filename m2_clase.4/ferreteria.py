import threading
from abc import ABC, abstractmethod

#patron singleton
class sistemaFacturacion:

    _instancia = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs): 
        
        with cls._lock:
            if cls._instancia is None:
                cls._instancia = super(sistemaFacturacion, cls). __new__(cls)
                cls._instancia._inicializacionHistorico()
            return cls._instancia
        
    def _inicializacionHistorico(self):
        self.historial = []
        print("sistema de facturacion inicializado")

    def registrarOperacion(self, operacion):
        self.historial.append(operacion)
        print(f"operacion registrada {operacion}")

#clase abstracta = superclase
class ProcesoNegocio(ABC):

    @abstractmethod
    def ejecutar(self):
        pass

class ProcesoPedido(ProcesoNegocio):
    
    def ejecutar(self):
        print("procesando pedido...")
        return "pedido procesado"
    
class ProcesarFactura(ProcesoNegocio):

    def ejecutar(self):
        print("procesando factura")
        return "factura procesada"
    
#crear fabrica (patron de diseño factory)
class FabricaProcesoNegocio:

    @staticmethod
    def crearProceso(tipoProceso):

        if tipoProceso == "pedido":
            return ProcesoPedido()
        elif tipoProceso == "factura":
            return ProcesarFactura()
        else:
            raise ValueError(f"el proceso {tipoProceso} no existe")
        
if __name__ == "__main__":

    sistema_facturacion = sistemaFacturacion()
    

    proceso1 = FabricaProcesoNegocio.crearProceso("pedido")
    proceso2 = FabricaProcesoNegocio.crearProceso("factura")

    resultadoPedido1 = proceso1.ejecutar()
    sistema_facturacion.registrarOperacion(resultadoPedido1)

    resultadoPedido2 = proceso2.ejecutar()
    sistema_facturacion.registrarOperacion(resultadoPedido2)

    print("\n***historico de procesos de negocio***\n")
    for operacion in sistema_facturacion.historial:
        print(f"transaccion: {operacion}")


