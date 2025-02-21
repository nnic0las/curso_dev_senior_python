import tkinder as tk
from tkinder import messagebox
import datetime

class Vehiculo:
    def __init__(self, placa, hora_entrada):
        self.placa = placa
        self.hora_entrada = hora_entrada

        def calcular_tiempo(self):
            hora_salida = datetime.datatime.now()
            tiempo_total = hora_salida - self.hora_entrada
            return tiempo_total.total_seconds() / 60

class ParqueaderoApp:
    #podemos llamarla como ventana o root
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Control de Parqueadero")
        self.ventana.geometry("500x400")

        self.vehiculos = {}

        #Entrada de la placa
        tk.Label(ventana, text="Placa del Vehiculo:").pack(pady=5)#texto
        self.entry_placa = tk.Entry(ventana) #caja de texto
        self.entry_placa.pack(pady=5)

        #botones
        tk.Button(ventana, text="Registro Entrada", command="").pack(pady=5)
        
root = tk.Tk()
app = ParqueaderoApp(root)
root.mainloop()

