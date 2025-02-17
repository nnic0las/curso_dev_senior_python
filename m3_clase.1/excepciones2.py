
#1
#app que permita dividir dos numeros 
"""
def division_cero(numero1, numero2):
    try: 
        resultado = numero1 / numero2
        print(resultado)
    except ZeroDivisionError as e:
        print("la division entre cero no se puede lograr")
        return None
    
division_cero(2,0)

#==================================================

#2
#excepciones multiples
def division_segura(numero1, numero2):
    try:
        numerador = int(input("ingrese el numerador de la division: "))
        denominador = int(input("ingrese el denominador de la division"))
        resultado = numerador / denominador
        print(f"el resultado de la division de {numerador} entre {denominador} es {resultado}")
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error {e}")

division_segura()

#==================================================

#3
#manejo de excepciones especificas "Exception"<<no es recomendable siempre ya que puede esconder errores>>

def abrir_archivo():
        try:
            with open("datos.txt","r") as archivo:
                contenido = archivo.read()
                numero = int(contenido.strip())
                print(numero)
        except Exception as e:
            print(f"Se produjo un error")

abrir_archivo()

#===============================================

#4
# uso else y finally 
def division_completa():
    try:
        numero = int(input("ingrese un numero: "))
        resultado = 10 / numero
        print(f"el resultado de la division es {resultado}")
    except ValueError as e:
        print(f"error: {e}")
    except ZeroDivisionError as e:
        print(f"error: {e}")
    else:
        print(f"el resultado de la division es {resultado}")
    finally:
        print("la operacion finalizo..... ")

division_completa()


#===============================================
#5
#app que permite procesar perdidos
#validar que el codigo de produco sea alfanumerico
#validar que la cantidad sea mayor a cero

def procesar_pedidos():
    try:
        codigo_producto = input("ingrese el producto: ")
        cantidad = int(input("ingrese la cantidad de "))

#validar que el codigo de produco sea alfanumerico
        if not codigo_producto.isalnum():
            raise ValueError("el codigo del producto debe ser alfanumerico")
        
#validar que la cantidad sea mayor a cero
        if cantidad <= 0:
            raise ValueError("la cantidad del producto debe ser mayor igual a cero")
        
        precio_unitario = 50
        total = precio_unitario * cantidad

    except ValueError as e:
        print(f"error al procesar el pedido: {e}")
    else:
        print(f"total a pagar: {total}") 
    finally:
        print("operacion finalizada")

procesar_pedidos() 

"""
#=====================================
#6
#exepciones personalizadas

class ErrorDePago(Exception):
    """gestion de excepciones"""
    pass

class PasarelaDePago():
    """simulacion una estrategia tegnologica de pago"""

    @staticmethod
    def procesar_pago(numero_tarjeta, monto):

        if not numero_tarjeta.startswith("4"):
            raise ErrorDePago("el numero de la tarjeta no es valido")

        if monto <= 0: 
            raise ErrorDePago("El monto debe ser mayor a cero")
            
        return f"pago de ${monto} fue procesado con exito"

def procesarPagoCliente(nombre_cliente, numero_tarjeta, monto):
    try:
        print(f"Iniciando el proceso de pago para {nombre_cliente}")
        resultado = PasarelaDePago.procesar_pago(numero_tarjeta, monto)

    except ErrorDePago as e:
        print(f"Error al procesar el pago {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado {e}")
    else:
        print(resultado)
    finally:
        print("Registro finalizado")

if __name__ == "__main__":
    procesarPagoCliente("nicolas", "4321", 99.00)
    procesarPagoCliente("luisa", "123", 100.00)






