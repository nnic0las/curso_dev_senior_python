#listas en python []
productos = ["carne", "papa", "tomate"]
productos.append("yuca")
print(productos)

#tupla en python () las tuplas son inmutables
empleado = (1010, "luis morelo", "director")
print(empleado)

#set (conjuntos) en python {}
categorias = {"terror", "drama", "scfc"}
categorias.add("suspenso")
print(categorias)

#diccionario (dict) en python
clientes = {
    "id": 1010, 
    "nombre": "luis",
    "apellido": "morelo"

}
print(clientes)
#para agregar un valor creamos la clave y luego el valor 
clientes["email"] = "luis@gmail.com"
print(clientes)

