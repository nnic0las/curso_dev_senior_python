from datetime import datetime
import statistics

class Tarea:

##funcion de inicializacion o metodo constructor
    def __init__(self, nombre, fechaLimite, categorias, horasDedicadas):
        self.nombre = nombre 
        self.fechaLimite = fechaLimite
        self.categorias = categorias
        self.horasDedicadas = horasDedicadas

##funcion para agregar una tarea 
def agregarTarea(listaTareas):
    nombre = input('ingrese el nombre de la tarea')
    fechaLimite_str = input('ingrese la fecha limite de la tarea(DD/MM/AAAA): ')
    try:
        fechaLimite = datetime.strptime(fechaLimite_str, "%d/%m/%Y ")
    except ValueError:
        print("fevha no valida.")
        return
    
    categorias = input("ingrse la categoria de la tarea (estido, trabajo, personal, otras)")
    horasDedicadas_str = input("ingrese las horas dedicadas separadas en comas: ")

    try:
        horasDedicadas = list(map(float, horasDedicadas_str.split(",")))
    except ValueError:
        print("horas no validas")
        return
    
    ##crear un objeto y agregarlo a la lista de tareas
    tarea = Tarea(nombre, fechaLimite, categorias, horasDedicadas)
    listaTareas.append(tarea)
    print("tarea agregada con exito ")

##visualizar las tareas 
def VisualizarTareas(listaTareas):
    if not listaTareas:
        print("no hay tareas reguistradas ")
        return      
    for i, tarea in enumerate(listaTareas, start=1):
        print(f"\nTareas {i}")
        print(f"nombre: {tarea.nombre}")
        print(f"fecha limite: {tarea.fechaLimite.strftime('%d, %m, %Y')}")
        print(f"categoria: {tarea.categorias}")
        print(f"horas dedicadas: {tarea.horasDedicadas}")

def analizarHoras(listaTareas):
    if not listaTareas:
        print("no hay tareas reguistradas ")
        return
    
    for tarea in listaTareas:
        promedio = statistics.mean(tarea.horasDedicadas)
        maximo = max(tarea.horasDedicadas)
        minimo = min(tarea.horasDedicadas)
        print(f'\nanalisis de {tarea.nombre}')
        print(f"promedio de horas: {promedio}")
        print(f"maximo de horas {maximo} ")
        print(f"minimo de horas {minimo}")

## generar un informe creando un archivo (.txt)
def gernerarInforme(listaTareas):
    if not listaTareas:
        print("no hay tareas reguistradas ")
        return

## abrir un archivo txt para escribir un informe 

with open('informe_tareas.txt', 'w') as archivo:
    for tarea in listaTareas:
        archivo.write(f"nombre: {tarea.nombre}\n")
        archivo.write(f"fecha limite: {tarea.fechaLimite.strftime ('%d, %m, %Y')}\n")
        archivo.write(f"categoria: {tarea.categoria}\n")
        archivo.write(f"horas dedicadas: {tarea.horasDedicadas}\n")
        archivo.write("\n")
print('informe generado como "informe_tareas.txt"')

def menu():

    listaTareas = []
    while True:
        print("\nmenu de opciones: ")
        print("1. agregar tarea ")
        print("2. visualizar tareas ")
        print("3. analizar horas dedicadas ")
        print("4. generar informe ")
        print("5. salir ")

        opcion = int(input("seleccione una opcion: "))

        if opcion == 1: 
            agregarTarea(listaTareas)
        elif opcion == 2: 
            VisualizarTareas(listaTareas)
        elif opcion == 3: 
            analizarHoras(listaTareas)
        elif opcion == 4: 
            gernerarInforme(listaTareas)
        elif opcion == 5: 
            print("saliendo del programa...")
            break
        else:
            print('opcion invalida')

if __name__ == "__main__":
    menu()




        
