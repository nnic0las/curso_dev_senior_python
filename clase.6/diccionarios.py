conceptosDeProgramacion = {
    'POO' : 'Programacion orienta a objetos',
    'IDE' : 'Entorno de desarrollo integrado',
    'DBMS': 'Sisresma de gestion de bases de datos'
}

print(conceptosDeProgramacion)
print(len(conceptosDeProgramacion))

print(conceptosDeProgramacion['IDE'])

##para obtener alguna de las literales de indormacion en un diccionario
print(conceptosDeProgramacion.get('POO'))

##funcion para modificar elementos de un diccionario 
conceptosDeProgramacion['DBMS'] = 'Database Managment System'
print(conceptosDeProgramacion)

## si queremos imprimir solos los id utilizamos un for 
for keys in conceptosDeProgramacion:
    print(keys)

##para imprimir el id y el value usamos for de la siguiente manera
for key, evalue in conceptosDeProgramacion.items():
    print(key,evalue)

