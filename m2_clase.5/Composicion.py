class Vehiculos:

    def __init__(self, motor):
        self.motor = motor

    def encender(self):
        print("encender el vehiculo ")
        self.motor.iniciar()

class Motor:    
    def __init__(self):
        pass

    def iniciar(self):
        pass

class MotorGasolina(Motor):
    def __init__(self):
        pass

    def iniciar(self):
        print("motor de gasolina encendido..")

class MotorElectrico(Motor):
    def __init__(self):
        pass

    def iniciar(self):
        print("motor electrico encendido..")

motor_gasolina = MotorGasolina() 
motor_electrico = MotorElectrico()

auto_gasolina = Vehiculos(motor_gasolina)
auto_electrico = Vehiculos(motor_electrico)

auto_gasolina.encender()
auto_electrico.encender()

        