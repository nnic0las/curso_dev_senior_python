class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def asignar_tarea(self, tarea):
        self.tareas.append(tarea)

    def realizar_tarea(self):
        print(f"{self.nombre}, esta desarollando las siguientes tareas")
        for tarea in self.tareas: 
            print (f"{tarea.ejecutar()}")

class Tareas:
    def __init__(self):
        pass

    def ejecutar(self):
        pass

class TrabajoProyecto(Tareas):

    def __init__(self):
        pass
    
    def ejecutar(self):
        return ("Trabajando en un proyecto")
    
class Capacitacion(Tareas):

    def __init__(self):
        pass

    def ejecutar(self):
        return "Tomando una capacitacion"
    
class Evaluacion(Tareas):

    def __init__(self):
        pass

    def ejecutar(self):
        return "Desarrollando una evaluacion del personal "
    
proyecto = TrabajoProyecto()
capacitacion = Capacitacion()
evaluacion = Evaluacion()

empleado = Empleado("luis guillermo ")
empleado.asignar_tarea(proyecto)
empleado.asignar_tarea(evaluacion)
empleado.asignar_tarea(evaluacion)
empleado.asignar_tarea(capacitacion)

empleado.realizar_tarea()