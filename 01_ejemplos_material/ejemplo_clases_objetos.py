"""
Ejemplo base de Clases y Objetos.
Replica un caso sencillo de una clase con atributos y metodos.
"""


class Estudiante:
    def __init__(self, nombre, programa):
        self.nombre = nombre
        self.programa = programa
        self.activo = True

    def presentarse(self):
        estado = "activo" if self.activo else "inactivo"
        return f"Soy {self.nombre}, estudio {self.programa} y estoy {estado}."

    def retirar(self):
        self.activo = False


def main():
    estudiante_1 = Estudiante("Ana", "Analisis y Desarrollo de Software")
    estudiante_2 = Estudiante("Carlos", "Gestion de Redes")

    print("=== EJEMPLO CLASES Y OBJETOS ===")
    print(estudiante_1.presentarse())
    print(estudiante_2.presentarse())

    estudiante_2.retirar()
    print("\nTras actualizar estado del estudiante 2:")
    print(estudiante_2.presentarse())


if __name__ == "__main__":
    main()