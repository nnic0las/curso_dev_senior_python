class Animal:

    def __init__(self):
        pass


    def Hablar(self):
        pass

class Perro(Animal):

    def __init__(self):
        pass


    def hablar(self):
        return f"El perro hacer guau guau"

class Gato(Animal):

    def __init__(self):
        pass

    def hablar(self):
        return f"El gato hace meuw meuw"
    
animales = [Perro(),
            Gato()]


for animal in animales:
    print(animal.hablar)