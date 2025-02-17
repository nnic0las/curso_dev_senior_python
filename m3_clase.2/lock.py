import logging
from dataclasses import dataclass, field

"""
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("Este mensaje es del DEBUG")
logging.info("Este mensaje es del INFO")
logging.warning("Este mensaje es del WARNING")
logging.error("Este mensaje es del ERROR")
logging.critical("Este mensaje es del critical")

"""

#app que permite llevar seguimiento de compras/fallos en el proceso de transaccion
#esta app, resgistra  la cantidad de productos comprados, confirmacion de compra y errores en estas transacciones 

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="registro.log",
    filemode="a"#este parametro "a" va a guardar todas las transacciones y va a crecer tantas veces nosostros ejecutemos esa aplicacion
    ) 

@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int
    
    def comprar(self, cantidad : int):
        if cantidad > self.cantidad:
            logging.error(f"Error: No hay suficiente cantidad del producto {self.nombre}. El stock disponible es de {self.cantidad}")
            print(f"Error: No hay suficiente cantidad del producto {self.nombre}. El stock disponible es de {self.cantidad}")

            raise ValueError(f"Error: No hay suficiente cantidad del producto {self.nombre}. El stock disponible es de {self.cantidad}")
        else: 
            self.cantidad -= cantidad
            logging.info(F"Lacompra fue exitosa. El stock restante es {self.cantidad}")
            print(F"Lacompra fue exitosa. El stock restante es {self.cantidad}")

        return self.precio * cantidad

@dataclass
class Tienda:
    productos: list[Producto] = field(default_factory = list)
    
    def agregar_producto(self, producto = Producto):
        self.productos.append(producto)
        logging.debug(f"{producto.nombre} agregado con exito. El precio es de {producto.precio} - cantidad {producto.cantidad} unidades en stock")
        print(f"{producto.nombre} agregado con exito. El precio es de {producto.precio} - cantidad {producto.cantidad} unidades en stock")

    
    def realizar_compra(self, nombre_producto: str, cantidad: int):
        producto = next((p for p in self.productos if p.nombre == nombre_producto), None)
        if producto:
            try:
                total = producto.comprar(cantidad)
                logging.info(f"Compra realizada: {cantidad} unidades de {nombre_producto} con un  total de ${total}")
                print(f"Compra realizada: {cantidad} unidades de {nombre_producto} con un  total de ${total}")

                return total
            except ValueError as e:
                logging.error(f"Error al efectuar la compra: {e}")
                print(f"Error al efectuar la compra: {e}")

            else:
                logging.warning(f"El producto fuera de stock")
                print(f"El producto fuera de stock")

if __name__ == "__main":
    tienda = Tienda()

    inventario_portatil = Producto(nombre="Portatil", precio=1000, cantidad=10)
    tienda.agregar_producto(inventario_portatil)
    tienda.realizar_compra("Portatil", 4)
