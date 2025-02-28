import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)

@dataclass
class Vendedor:
    nombre: str
    ventas_totales: float

    def calculo_comision(self) -> float:
        if self.ventas_totales > 10000:
            comision = self.ventas_totales * 0.1
            logging.debug(f"{self.nombre} ha alcanzado el umbral de ventas la comision calculada es de {comision}")
        else:
            comision = self.ventas_totales * 0.05
            logging.debug(f"{self.nombre} no ha alcanzado el umbral de ventas la comision calculada e de {comision}")
        return comision

if __name__ == "__main__":
    vendedor = Vendedor("piter", 12000)
    print(f"la comision de {vendedor.nombre}: {vendedor.calculo_comision()}")

