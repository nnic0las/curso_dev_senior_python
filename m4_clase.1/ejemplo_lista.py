#app gestion de pedidos de una tienda
def agregar_pedido(pedidos: list[str], nuevo_pedido: str) -> list[str]:
    pedidos.append(nuevo_pedido)
    return pedidos

def eliminar_pedido(pedidos: list[str], pedido_a_eliminar: str) -> list[str]:
    if pedido_a_eliminar in  pedidos:
        pedidos.remove(pedido_a_eliminar)
    else:
        print("el pedido no se encuentra en la lista")
    return pedidos

def buscar_pedido(pedidos: list[str], pedido_a_buscar: str) -> int:
    if pedido_a_buscar in pedidos:
        return pedidos.index(pedido_a_buscar)
    else:
        print("el pedido no se encuentra en la lista")
        return -1
    
def main():
    #lista inicial de pedidos
    pedidos_tienda = ["pedido 1", "pedido 3"]

    #agregar un nuevo pedido
    pedidos_tienda = agregar_pedido(pedidos_tienda, "pedido 2")

    #mostrar los elementos de la lista de forma desordenada 
    print("lsita actualizada de pedidos", pedidos_tienda)

    #ordene la lista
    pedidos_tienda.sort()
    print("lsita actualizada de pedidos ordenada", pedidos_tienda)

    #buscar un pedido en especifico
    pedido_a_buscar = "pedido 3"
    indice = buscar_pedido(pedidos_tienda, pedido_a_buscar)
    if indice != -1:
        print(f"el {pedido_a_buscar} sen encuentra en la posicion {indice}")

    #eliminar un pedido 
    pedido_a_eliminar = "pedido 1"
    pedidos_tienda = eliminar_pedido(pedidos_tienda, pedido_a_eliminar)
    print(f"la lista resultante luego de eliminar a {pedido_a_eliminar} es {pedidos_tienda}")







if __name__ == "__main__":
    main()
