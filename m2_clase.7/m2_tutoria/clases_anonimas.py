Producto = type("Productos", (), {"Nombre": None, "Precio": None})

Producto1= Producto()
Producto1.Nombre = "laptop"
Producto1.Precio = 1500

print(f"Producto: {Producto1.Nombre}, Precio: {Producto1.Precio}")

