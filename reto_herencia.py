print("=== PROGRAMA: JERARQUÍA DE PRODUCTOS ===\n")

# ── Clase base: contiene atributos y métodos comunes ─────────
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre  = nombre
        self.precio  = precio
        self.stock   = stock

    def mostrar_info(self):
        return (f"Producto : {self.nombre}\n"
                f"Precio   : ${self.precio:,.0f}\n"
                f"Stock    : {self.stock} unidades")

    def hay_stock(self):
        return self.stock > 0

# ── Clase hija: hereda de Producto y agrega fecha_caducidad ──
class Alimento(Producto):
    def __init__(self, nombre, precio, stock, fecha_caducidad):
        # Llama al constructor del padre para inicializar
        # nombre, precio y stock
        super().__init__(nombre, precio, stock)

        # Atributo específico de Alimento
        self.fecha_caducidad = fecha_caducidad

    def mostrar_info(self):
        # Reutiliza la info del padre y agrega fecha de caducidad
        info_base = super().mostrar_info()
        return (f"{info_base}\n"
                f"Caducidad: {self.fecha_caducidad}")

# ── Clase hija: hereda de Producto y agrega garantia ─────────
class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia):
        # Llama al constructor del padre
        super().__init__(nombre, precio, stock)

        # Atributo específico de Electronico
        self.garantia = garantia

    def mostrar_info(self):
        # Reutiliza la info del padre y agrega garantía
        info_base = super().mostrar_info()
        return (f"{info_base}\n"
                f"Garantía : {self.garantia} meses")

# ── Creación de instancias ────────────────────────────────────
print("=== CREANDO PRODUCTOS ===")

# Instancia de la clase base
producto1 = Producto("Cuaderno", 3500, 50)

# Instancia de Alimento
producto2 = Alimento("Yogur Natural", 2800, 30, "2026-06-15")

# Instancia de Electronico
producto3 = Electronico("Audífonos Sony", 150000, 10, 12)

# ── Mostrar información ───────────────────────────────────────
print("\n=== INFORMACIÓN DE PRODUCTOS ===")

print("\n" + producto1.mostrar_info())
print("\n" + producto2.mostrar_info())
print("\n" + producto3.mostrar_info())

# ── Verificar stock ───────────────────────────────────────────
print("\n=== VERIFICANDO STOCK ===")

for producto in [producto1, producto2, producto3]:
    if producto.hay_stock():
        print(f"{producto.nombre}: Hay stock disponible.")
    else:
        print(f"{producto.nombre}: Sin stock.")