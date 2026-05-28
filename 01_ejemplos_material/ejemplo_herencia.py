"""
Ejemplo de herencia en POO.
Incluye clase base y dos clases hijas.
"""


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:,.0f}"


class Alimento(Producto):
    def __init__(self, nombre, precio, fecha_caducidad):
        super().__init__(nombre, precio)
        self.fecha_caducidad = fecha_caducidad

    def mostrar_info(self):
        return f"{super().mostrar_info()} | Caduca: {self.fecha_caducidad}"


class Electronico(Producto):
    def __init__(self, nombre, precio, garantia_meses):
        super().__init__(nombre, precio)
        self.garantia_meses = garantia_meses

    def mostrar_info(self):
        return f"{super().mostrar_info()} | Garantia: {self.garantia_meses} meses"


def main():
    items = [
        Producto("Cuaderno", 3500),
        Alimento("Yogur Natural", 2800, "2026-06-15"),
        Electronico("Audifonos Sony", 150000, 12),
    ]

    print("=== EJEMPLO HERENCIA ===")
    for item in items:
        print(item.mostrar_info())


if __name__ == "__main__":
    main()