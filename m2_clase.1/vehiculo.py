##herencia
class Vehiculo:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def descripcion(self):
        return f"este vehiculo es de tipo {self.tipo}"
    
class Moto(Vehiculo):
    
    def __init__(self, tipo, marca):
        super().__init__(tipo)
        self.marca = marca


moto1 = Moto("motocicleta","ducatti")
print(moto1.descripcion())

        