#conjuntos o set en python
#app de gestion de clientes(unicos) de una campaña de mercadeo

from typing import Set 

def obtener_clientes_unicos(clientes: Set[str], nuevos_clientes: Set[str]) -> Set[str]:
    return clientes.union(nuevos_clientes)

def gestionar_clientes(clientes: Set[str]) -> None:

    #agregar un cliente
    clientes.add("pedro")
    print("clientes despues de agregar a pedro:", clientes)
    
    #agregar un cliente duplicado
    clientes.add("carlos")
    print("clientes despues de intentar agregar a carlos:", clientes)

    #uso de la funsion remove para eliminar un cliente (si existe, y si no error)
    cliente = "ana"
    clientes.remove(cliente)
    print("clientes despues de eliminar a ana con el metodo remove: ", clientes)

    #uso de la funsion discard para eliminar un elemento del set
    cliente2 = "luis"
    clientes.discard(cliente2)
    print("clientes despues de eliminar a luis con el metodo discard: ", clientes)

    #uso del metodo pop para mostrar un elemento del set y posterior lo borra automaticamente 
    cliente_removido = clientes.pop()
    print(f"cliente removido aleatoriamente: {cliente_removido}")
    print("clientes restantes:", clientes)

    #borrar todos los elementos del set
    clientes.clear()
    print("clientes despues del metodo clear:", clientes)

def main():

    clientes_antiguos = {"carlos", "ana", "luis"}
    clientes_nuevos = {"luis", "maria", "jorge"}
    clientes_finales = obtener_clientes_unicos(clientes_antiguos, clientes_nuevos)
    print("la lista actualizada de clientes es: ", clientes_finales)

    gestionar_clientes(clientes_finales)

if __name__ == "__main__":
    main()

