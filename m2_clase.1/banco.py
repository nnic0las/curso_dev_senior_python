class Banco:

    tasaInteres = 0.03

    def __init__(self, nombre, nuevaTasa):
        self.nombre = nombre
        self.nuevaTasa = nuevaTasa


    @classmethod
    def cambiarTasa(cls, nuevaTasa):
        cls.tasaInteres = nuevaTasa

    @classmethod
    def comversionDolaresEuros(dolares):
        return dolares * 0.85
    
    