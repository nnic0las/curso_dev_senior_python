productos = [
    {"nombre": "laptop", "precio":1500},
    {"nombre": "celular", "precio":500},
    {"nombre": "tablet", "precio":2000}

]
productos_ordenados = sorted(productos, key=lambda x: x["precio"])
print(productos_ordenados)