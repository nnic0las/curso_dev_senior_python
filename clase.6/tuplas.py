paises = ('colombia','mexico','ecuador','venezuela')
print(type(paises))
print(len(paises))
print(paises[2])
print(paises[-1])

##para que la tupla nos saque la literal de informacion en forma vertical 
for pais in paises:
    print(pais)

##para modificar una tupla la convertimos en una lista
paisesLista = list(paises)
paisesLista[1] = 'argentina'

##luego de haber modificado la lista la volvemos a comvertir en tupla
paises = tuple(paisesLista)
print(paises)