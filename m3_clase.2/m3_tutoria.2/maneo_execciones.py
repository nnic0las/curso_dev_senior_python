"""
#el bloque try se utiliza para embolver el codigo que puede generar excepciones, si ocurre unas 
#excepcion, se ejecuta el bloque except


try:
    num = int(input("Ingrese un numero: "))

    print(f"El doble es : {num*2}")
except ValueError:
    print("Error: No ingresastes un numero valido")

#el bloque else se ejecuta solo si no ocurre ninguna excepcion dentro del bloque try
else:
    print(f"El numero ingresado es: {num}")

#===================================================================================

#bloque finally se ejecuta siempre independientemente de si ocurre o no ocurre una excepcion
#es util para liberar recursos, cerrar archivos, conexiones a bases de datos, etc
try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no existe")
finally:
    try:        
        archivo.close()
        print("Archivo cerrado")
    except NameError:
        print("el archivo no se abrio, no hay que cerrar")

#==================================================================================
"""
#manejo de multiples excepciones 
#puedes manejar diferentes tipos de excepciones en el bloque separado por excep o agruparlos en una tuplas 
"""
try:
    num = int(input("Ingresa un numero: "))
    resultado = 10/num
except ValueError:
    print("Error: no ingresastes un numero valido..")
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")


try:
    num = int(input("Ingresa un numero: "))
    resultado = 10/num
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
"""
#==============================================================================

#creacion de excepciones personalizadas

class MisExcepciones(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

try:
    edad = int(input("ingrese su edad"))
    if edad < 0:
        raise MisExcepciones("la edad no puede ser negativa")
    print(f"tu edad es {edad}")
except MisExcepciones as e:
    print(f"Error: {e}")

#recomendaciones 
#usar las excepciones solo para situaciones execionales, no como logica de control 
#siempre usar el finally ara liberar recursos
#se especifica al capturar error








