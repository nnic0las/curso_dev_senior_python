#importamos la libreria
import tkinter as tk

def convertir():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        resultado.config(text=f"Resultado: {fahrenheit: .2f}ºF")
    except:
        resultado.config(text="Ingrese un numero valido")



#configuracion de la ventana 
#creamos la ventana de la aplicacion
#podemos llamaral como ventana o root
root = tk.Tk()
#asignamos un titulo a la ventana
root.title("Conversor de temperatura")
#creamos los parametro o tamaño de la ventana
root.geometry("300x200")


#widgets
#nos permite pedir datos al usuario y para que nos salga en la ventada utilizamos el .pack(pady=)
tk.Label(root, text="Ingrese temperatura en ºC:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

#con esta linea de codigo pordemos crear un boton para ejecutar la funcion
tk.Button(root, text="convertir", command= convertir).pack(pady=5)
resultado = tk.Label(root, text="resultado: ")
resultado.pack(pady=5)
#llamamos la ventana
root.mainloop()