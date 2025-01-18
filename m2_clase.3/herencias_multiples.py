class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descripcion(self):
        return f"Libro: {self.titulo} Autor: {self.autor}"

        #opcional
    def __str__(self):
        return f"Libro: {self.titulo} Autor: {self.autor} str"

class librosDigiral(Libro): #subclase

    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.formato = formato

    def descripcion(self):
        return f"Libro: {self.titulo} Autor: {self.autor} Formato: {self.formato}"

    def __str__(self):
        return f"Libro: {self.titulo} Autor: {self.autor} Formato: {self.formato} str"
    
libro1 = Libro("La peste","Alberto Campo")
librosDigiral1 = librosDigiral("El conde de monte cristo", "Alejandro Dumas", "PDF")

print(libro1.__str__())
print(libro1.descripcion())

print(librosDigiral1.__str__())
print(librosDigiral1.descripcion())
