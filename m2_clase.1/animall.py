class Animall:

    cantidadAnimales = 0

    def __init__(self, name):
        self.name = name 
        Animall.cantidadAnimales +=1

##decoradores
    @classmethod

    def totalAnimales(cls):
        return f"tengo {cls.cantidadAnimales} animalitos"

animalito1 = Animall("ron")
animalito2 = Animall("rayo")

print(animalito2.name)
print(Animall.totalAnimales())
