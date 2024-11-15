estudiantes = []
cursos = ['java','python']
docentes = []
horarios = []

##funsion para matricular un estudiante 

def matricularEstudiante():
    nombre = input('Digite el nombre del estudiante: ')
    print('selecciones el curso a matricular: ')
    for i,curso in enumerate(cursos):
        print(f'{i+1}: {curso}')

    cursoSeleccionado = int(input('ingrese el numero del curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado-1]
        ##diccionario
        estudiante = {'nimbre': nombre, 'curso': curso}
        estudiantes.append(estudiante)
        print(f'Estudiante: {nombre}, matriculado en el curso: {curso}')
    else: 
        print(f'opcion de curso no valida, cursos aviles {len(cursos)}')

##funcion para asignar un docente a un curso
def asignarDocente():
    print('seleccionar el curso al que desea asignar un docente: ')
    for i,curso in enumerate(cursos):
        print(f'{i+1}: {curso}')
    
    cursoSeleccionado = int(input('ingrese el numero del curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado-1]
        nombreDocente = input('ingrese el nombre del docente: ')
        docente = {'nimbre': nombreDocente, 'curso': curso}
        docentes.append(docente)
        print(f'docente: {nombreDocente}, asignado a el curso: {curso}')
    else: 
        print(f'opcion de curso no valida, cursos aviles {len(cursos)}')  

##funsion para asignar horario a un curso
def asignarHorario():
    print('seleccionar el curso al que se le va a signar e horario: ')
    for i,curso in enumerate(cursos):
        print(f'{i+1}: {curso}')
    cursoSeleccionado = int(input('ingrese el numero del curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado-1]
        dias = input('ingrese los dias de clase (ej: martes y jueves): ')
        hora = input('ingrese la hora de la clase (ej: 6 pm): ')
        horario = {'curso': curso, 'dias': dias, 'hora': hora}
        horarios.append(horario)
        print(f'horario asignado al curso: {curso}, {dias} a las {hora}')
    else:
        print(f'opcion de curso no valida, cursos aviles {len(cursos)}')


##mostras datos 
def mostrarEstudiantes():
    if estudiantes:
        print('lista de estudiantes matriculados ')
        for estudiante in estudiantes:
            print(f'estudiante: {estudiante['nombre']}, curso: {estudiante['curso']}')
    else:
        print('no hay estudiantes matriculados')

def mostrarDocentes():
    if docentes:
        print('lista de docentes asignados')
        for docente in docentes:
            print(f'docente : {docente['nombre']}, curso: {docente['curso']}')
    else:
        print('no hay docentes asignados')


def mostrarHorario():
    if horarios:
        print('\nhorarios de los cursos ')
        for horario in horarios:
            print(f'curso: {horario['curso']}, dias: {horario['dias']}, hora: {horario['hora']}')
    else:
        print('no hay horarios asignados ')


##menu
while True:
    print('\n sistema de matricula de dev senior')
    print('\n 1. matriculas estudiante.')
    print('\n 2. asignar docente a un curso.')
    print('\n 3. asignar horario a un curso.')
    print('\n 4. mostrar la lista de los estudiantes matriculados.')
    print('\n 5. mostras la lista de docentes asignados.')
    print('\n 6. mostrar horarios de los cursos.')
    print('\n 7. salir.')
    






