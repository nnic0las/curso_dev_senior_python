class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def encender(self):
        print(f"El motor tipo {self.tipo} se ha encendido")

class Rueda:
    def __init__(self, tamaño):
        self.tamaño = tamaño

    def girar(self):
        print(f"La rueda de tamaño {self.tamaño} esta girando")

class Coche:
    def __init__(self, motor, ruedas):
        self.motor = motor
        self.ruedas = ruedas

    def iniciar_viaje(self):
        self.motor.encender()
        for rueda in self.ruedas:
            rueda.girar()

        print("El coche a comenzado a moverse")

motor_deportivo = Motor("V10")

tipo_ruedas = int(input("Elija el tipo de ruedas que va a usar (10-50):"))

ruedas_pequeñas = Rueda(tipo_ruedas), Rueda(tipo_ruedas), Rueda(tipo_ruedas), Rueda(tipo_ruedas) 

coche_deportivo = Coche(motor_deportivo, ruedas_pequeñas)
coche_deportivo.iniciar_viaje()

