lenguajes = {'java', 'python', 'javaScript'}
print(lenguajes)
print(len(lenguajes))
print('java' in lenguajes)
lenguajes.add('Go')
print(lenguajes)

##para que nos arroje la literal de informacion de forma vertical utilizamos un for
for lenguaje in lenguajes:
    print(lenguaje)

##para eliminar literal de informacion en un set
lenguajes.remove('java')
print(lenguajes)

lenguajes.discard('python')
print(lenguajes)

