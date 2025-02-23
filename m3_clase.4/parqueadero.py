import tkinter as tk
from tkinter import  ttk,messagebox
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
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Parqueadero")
        self.root.geometry("500x400")

        self.vehiculos = {}

        #Entrada de la placa
        tk.Label(root, text="Placa del Vehiculo:").pack(pady=5)#texto
        self.entry_placa = tk.Entry(root) #caja de texto
        self.entry_placa.pack(pady=5)

        #botones
        tk.Button(root, text="Registro Entrada", command=self.registro_entrada).pack(pady=5)
        tk.Button(root, text="Registro Salida", command=self.registrar_salida).pack(pady=5)

        #Tabla de vehiculos
        self.tree = ttk.Treeview(root, columns=("Placa", "Hora de Entrada", "Hora de salida"), show="headings")
        self.tree.heading("Placa", text="Placa")
        self.tree.heading("Hora de Entrada", text="Hora de Entrada")
        self.tree.heading("Hora de Salida", text="Hora de Salida")

        self.tree.pack(pady=10, fill="both", expand=True)

    def registro_entrada(self):
        placa = self.entry_placa.get.upper()
        if placa and placa not in self.vehiculos:
            hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
            self.vehiculos[placa] = Vehiculo(placa, datetime.datetime.now())

            self.tree.insert("","end", iid=placa, values=(placa, hora_actual) )
        else: 
            messagebox.showerror("Error", "placa invalida o ya registrada")

    def registrar_salida(self):
        placa = self.entry_placa.get().upper()
        if placa in self.vehiculos:
            Vehiculo = self.vehiculos.pop(placa)
            tiempo_parque = Vehiculo.calcular_tiempo()

            #eliminar de la tabla
            self.tree.delete(placa)

            messagebox.showinfo("Salida ",f"vehiculo {placa} Salio. \nTiempo: {tiempo_parque: .2f}
            minutos")
        else:
            messagebox.showerror("Error", "Vehiculo no encontrado")



        
root = tk.Tk()
app = ParqueaderoApp(root)
root.mainloop()

