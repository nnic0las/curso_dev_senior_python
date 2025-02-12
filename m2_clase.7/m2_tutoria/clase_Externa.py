class Externa:
    def __init__(self, mensaje):
        self.mensaje = mensaje
    
    class Interna:
        def __init__(self, externa):
            self.externa = externa

        def mostrar_mensaje(Self):
            print(f"Mensaje desde clase externa {Self.externa.mensaje}")

externa = Externa("hola desde la clase externa")
interna = Externa.Interna(externa)
interna.mostrar_mensaje()


