#implementar un sistema de monitoreo para facturacion c/manejo de execepciones por consola y .log file

import logging
from dataclasses import dataclass

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='ejercisio_lock.log',
    filemode='w'
    )

#crear un nuevo manejador "handler" para gestionar ensajes de auditoria por .log y por consola
console_handler = logging.StreamHandler() #crear una instancia, osea un nuevo manejador 
console_handler.setLevel(logging.DEBUG) #configurar el nivel de logging, en este caso, el nivel mas leve
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',)) # dando formato de salida logging
logging.getLogger().addHandler(console_handler) #agregando la instancia console_handler al manejador principal

@dataclass
class Factura:
    cliente: str
    cantidad: int
    precio_unitario: float

    def procesar(self):
        try:
            logging.info(f"iniciando proceso de facturacion para el cliente {self.cliente}")

            if self.cantidad <= 0:
                raise ValueError(f"La cantidad de producto debe ser mayor a cero")
            if self.precio_unitario <= 0:
                raise ValueError(f"Precio debe ser mayor a cero")
            
            total = self.cantidad * self.precio_unitario
            logging.info(f"Factura fue procesada con exito. total de la compra {total} - cliente: {self.cliente}")
        except ValueError as e:
            logging.error(f"Error de validacion del cliente {self.cliente}: {e}")
        except ValueError as e:
            logging.critical(f"Error inesperado al momento de procesar la factura del {self.cliente}: {e}")
        finally:
            logging.info(f"El proceso de facturacion para {self.cliente} finalizo")

if __name__ == "__main__":
    factura1 = Factura("carlos", 10, 1500.25)
    factura1.procesar()

    factura2 = Factura("pedro", 5, 150)
    factura2.procesar()



