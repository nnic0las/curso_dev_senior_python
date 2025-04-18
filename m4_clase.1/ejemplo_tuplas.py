#app para registro de empleados
#lobreria typing nos trae las estruccturas de datos que vamos a utilizar 
from typing import Tuple

def obtener_info_empleado(empleado: Tuple[int, str, str]) -> Tuple:
    id_empleado, nombre_empleado, cargo_empleado = empleado
    print(f"Id: {id_empleado}, Nombre: {nombre_empleado}, Cargo: {cargo_empleado}")

#creamos una segunda tupla para el salario
def analizar_salario(salarios: Tuple[int, ...]) -> None:

    print(f"salarios tabulados: {salarios}")
    print(f"cantidad de salarios registrados: {len(salarios)}")
    print(f"el salario mas alto registrado es: {max(salarios)}")
    print(f"el salario mas bajo registrado es {min(salarios)}")
    print(f"la suma de todos los salarios registrados es: {sum(salarios)}")
    print(f"los salarios registrados de forma ordenada: {sorted(salarios)}")

    salario_a_buscar = 500
    print(f"el salario que tiene un valos de {salario_a_buscar} se encuentra {salarios.count(salario_a_buscar)} veces")

    if salario_a_buscar in salarios:
        print(f"el salario con un valor de {salario_a_buscar} se necuentra en la posicion {salarios.index(salario_a_buscar)}")

def main():
    empleado = (1111, "cristian rubio", "director de desarrollo")

    obtener_info_empleado(empleado)

    salarios_de_empleado = (500, 500, 100, 200, 300, 400, 500, 600)

    analizar_salario(salarios_de_empleado)

if __name__ == "__main__":
    main()

