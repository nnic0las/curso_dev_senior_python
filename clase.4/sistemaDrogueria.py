#codificacion camel cose
ventasTotales = 0 


#solicitar el nuero de productos 
numProductos = int(input('ingrese el numero de productos a gestionar: '))


#listas para almacenar la informacion 
nombres = []
precios = []
cantidades = []
print('ingreso inicial de productos a la tienda: ')

for i in range(numProductos):
    print(f'producto {i+1}: ')
    nombre = input('ingrese el nombre del producto: ').lower()
    nombres.append(nombre)
    precio = float(input('digite el precio del producto: '))
    precios.append(precio)
    cantidad = int(input('digite las cantidades del producto: '))
    cantidades.append(cantidad)

#ciclo principal menu 
while True:
    print('\n --- MENU GESTION DROGERIA--- ')
    print('1. vender producto')
    print('2. mostrar inventario ')
    print('3. mostrar ventas totales ')
    print('4. salir ')

    opcion = int(input('ingrse una opcion valida: '))

    if opcion == 1: 
        print('\n vender producto')
        nombreVenta = input('ingrese el nombre del producto a vender: ').lower()
        cantidadVender = int(input('ingrese la cantidad a vender: '))
        productoEncontrado = False

        for i in  range(len(nombre)):
            if nombres[i] == nombreVenta:
                productoEncontrado = True
                if cantidadVender <= cantidades[i]:
                    totalVenta = cantidadVender * precios[i]
                    ventasTotales += totalVenta
                    cantidades[i] -= cantidadVender
                    print(f'venta realizada. total de esta venta${totalVenta:.2f}')
                    print(f'quedan {cantidades[i]} unidades de {nombres[i]} en el inventario ')
                else:
                    print(f'cantidad insuficiente en inventario. ya que solo hay {cantidades[i]} ')          
                    break
        if not productoEncontrado:
            print('producto no encontrado en el inventario ')

    elif opcion == 2:
        print('\n inventario de producto')
        for i in  range(len(nombres)):
            print(f'producto {i+1}: {nombres[i].capitalize()}. precio : ${precios[i]:.2f}, cantidad: {cantidades[i]}')

    elif opcion == 3:
        print('\nventas totales acomuladas: ${ventasTotales:.2f}')

    elif opcion == 4:
        print('gracias por usar el sistema de gestion drogreria ') 
        break

    else:
        print('opcion invalida. ingresa (1-4)')



