from abc import ABC, abstractmethod

#clases abstractas, superclase
class Clases(ABC):
    @abstractmethod
    def operacion(self):
        pass
    
#creacion de subclases  
class ClaseA(Clases):
    def operacion(self):
        return "Esta es la clase A"
    
class ClaseB(Clases):
    def operacion(self):
        return "Esta es la clase B"
    
#clase factory: factoria, frabrica
class FrabricaClases:

    @staticmethod
    def crecionObjetos(tipoObjeto):
        if tipoObjeto == "a":
            return ClaseA()
        elif tipoObjeto == "B":
            return ClaseB()
        else:
            raise ValueError(f"la clase {tipoObjeto} no existe..")
        
objeto1 = FrabricaClases.crecionObjetos("A")
objeto2 = FrabricaClases.crecionObjetos("B")

print(objeto1.operacion())