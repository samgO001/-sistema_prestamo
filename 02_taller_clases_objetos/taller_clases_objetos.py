"""
Taller: Clases y Objetos.
Caso practico de una biblioteca con libros y operaciones basicas.
"""


class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if not self.disponible:
            return False, f"'{self.titulo}' ya esta prestado."
        self.disponible = False
        return True, f"Prestamo exitoso de '{self.titulo}'."

    def devolver(self):
        if self.disponible:
            return False, f"'{self.titulo}' ya estaba disponible."
        self.disponible = True
        return True, f"Devolucion exitosa de '{self.titulo}'."

    def descripcion(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({estado})"


def main():
    libro_1 = Libro("Clean Code", "Robert C. Martin")
    libro_2 = Libro("Python Crash Course", "Eric Matthes")

    print("=== TALLER: CLASES Y OBJETOS ===")
    print(libro_1.descripcion())
    print(libro_2.descripcion())

    ok, mensaje = libro_1.prestar()
    print(mensaje)
    print(libro_1.descripcion())

    ok, mensaje = libro_1.devolver()
    print(mensaje)
    print(libro_1.descripcion())


if __name__ == "__main__":
    main()