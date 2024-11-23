from datetime import datetime
import statistics


class Experimento:


    ##metodo constructor 
    def __init__(self, nombreExperimento, fechaDeRealizacion, tipoExperimento, resultadosExperimento):
        self.nombreExperimento = nombreExperimento
        self.fechaDeRealizacion = fechaDeRealizacion
        self.tipoExperimento = tipoExperimento
        self.resultadosExperimento = resultadosExperimento

## funcion agregar experimento 
def agregarExperimento(listaExperimentos):
    nombreExperimento = input('por favor ingrese el nombre del experimento: ')
    fechaDeRealizacion = input('ingresar la fecha de realizacion del proyecto (DD/mm/YYYY)')
    try:
        fechaDeRealizacion = datetime.strptime(fechaDeRealizacion, "%d/%m/%Y ")
    except ValueError:
        print("fecha no valida.")
        return
    
    tipoExperimento = input('ingrese el tipo de experimento que desea agregar: ')
    resultadosExperimento = input('ingrese los resultados obtenidos del experimento, separando cada resultado con coma (,):')

    try:
        resultadosExperimento(list(map(float, resultadosExperimento.split(","))))
    except ValueError:
        print("datos no validos...")
        return
    
## creacion de un objeto para almacenar la informacion
    experimento = Experimento(nombreExperimento, fechaDeRealizacion, tipoExperimento, resultadosExperimento)
    listaExperimentos.append(experimento)
    print("Experimento agregado con exito...")

## ver experimentos agregados 
def visualizarExperimentos(listaExperimentos):
    if not listaExperimentos:
        print("no hay experimentos agregados")
        return
    
    for i,experimento in enumerate(listaExperimentos, start=1):
        print(f"\nexperimento {i}")
        print(f"nombre: {experimento.nombreExperimento}")
        print(f"fecha limite: {experimento.fechaDeRealizacion.strftime('%d, %m, %Y')}")
        print(f"categoria: {experimento.tipoExperimento}")
        print(f"horas dedicadas: {experimento.resultadosExperimento}")

## analisis de resultados
def calcularEstadisticas(listaExperimentos):
    if not listaExperimentos:
        print("no hay experimentos agregados")
        return  
    
    for experimento in listaExperimentos:
        promedio = statistics.mean(experimento.resultadosExperimento)
        maximo = max(experimento.resultadosExperimento)
        minimo = min(experimento.resultadosExperimentos)
        print(f'\nestadisticas de {experimento.nombreExperimento}')
        print(f"promedio de los resultados: {promedio}")
        print(f"puntaje maximo de los resultados{maximo} ")
        print(f"puntaje minimo de los resultados{minimo}")


##generar un informe de los resultados .txt
def generarInforme(listaExperimentos):
    if not listaExperimentos:
        print("no hay experimentos agregados")
        return
    
with open('informe_resultados_experimento.txt','w') as archivo:
    for experimento in listaExperimentos:
        archivo.write(f"Nombre: {experimento.nombreExperimento}\n")
        archivo.write(f"Fecha de realizacion: {experimento.fechaDeRealizacion}\n")
        archivo.write(f"Tipos de experimento: {experimento.tipoExperimento}\n")
        archivo.write(f"resultados del experimento: {experimento.resultadoExperimento}\n")
        archivo.write("\n")

print("el informe solicitado con los analizis se a generado correctamente como 'informe_resultados_experimento.txt'")








