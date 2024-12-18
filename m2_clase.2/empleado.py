class Empleado:

    def __init__(self, nombre, salario):
        self._nombre = nombre
        self._salario = salario

    def mostrarInformacion(self):
        return f"Nombre: {self._nombre}, Salario: {self._salario}"
    
    def obtenerSalario(self):
        return self._salario

    def establecerSalario(self, nuevoSalario):
        if nuevoSalario < 1300000:
            return f"El salario no puede ser menor al salario minimo"
        self._salario = nuevoSalario
        return f"El nuevo salario es: {self._salario}"
    
empleado1 = Empleado("carlos", 1300000)

print(empleado1.mostrarInformacion())
print(empleado1.obtenerSalario())
print(empleado1.establecerSalario(1200000))
print(empleado1.establecerSalario(2500000))


        