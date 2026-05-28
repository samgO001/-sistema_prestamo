"""
Reto integrador: Sistema de Prestamos de Equipos.
Aplica POO con clases Equipo, Usuario y Prestamo, encapsulacion y colecciones.
"""

from datetime import date


class Equipo:
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria
        self._disponible = True

    @property
    def disponible(self):
        return self._disponible

    def marcar_prestado(self):
        if not self._disponible:
            return False
        self._disponible = False
        return True

    def marcar_devuelto(self):
        if self._disponible:
            return False
        self._disponible = True
        return True


class Usuario:
    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre


class Prestamo:
    def __init__(self, equipo, usuario):
        self.equipo = equipo
        self.usuario = usuario
        self.fecha_prestamo = str(date.today())
        self._estado = "ACTIVO"
        self.fecha_devolucion = None

    @property
    def estado(self):
        return self._estado

    def cerrar_prestamo(self):
        if self._estado != "ACTIVO":
            return False
        self._estado = "DEVUELTO"
        self.fecha_devolucion = str(date.today())
        return True


class SistemaPrestamos:
    def __init__(self):
        self.equipos = {}  # dict[str, Equipo]
        self.usuarios = {}  # dict[str, Usuario]
        self.prestamos = []  # list[Prestamo]

    def registrar_equipo(self, nombre, categoria):
        if nombre in self.equipos:
            return False, "El equipo ya existe."
        self.equipos[nombre] = Equipo(nombre, categoria)
        return True, f"Equipo '{nombre}' registrado correctamente."

    def registrar_usuario(self, documento, nombre):
        if documento in self.usuarios:
            return False, "El usuario ya existe."
        self.usuarios[documento] = Usuario(documento, nombre)
        return True, f"Usuario '{nombre}' registrado correctamente."

    def registrar_prestamo(self, nombre_equipo, documento_usuario):
        equipo = self.equipos.get(nombre_equipo)
        if equipo is None:
            return False, "Equipo no encontrado."
        if not equipo.disponible:
            return False, "Equipo no disponible."

        usuario = self.usuarios.get(documento_usuario)
        if usuario is None:
            return False, "Usuario no encontrado."

        equipo.marcar_prestado()
        prestamo = Prestamo(equipo, usuario)
        self.prestamos.append(prestamo)
        return True, "Prestamo registrado con exito."

    def devolver_prestamo(self, nombre_equipo):
        for prestamo in self.prestamos:
            if (
                prestamo.equipo.nombre == nombre_equipo
                and prestamo.estado == "ACTIVO"
            ):
                prestamo.cerrar_prestamo()
                prestamo.equipo.marcar_devuelto()
                return True, f"Equipo '{nombre_equipo}' devuelto correctamente."
        return False, "No existe prestamo activo para ese equipo."

    def consultar_equipos(self):
        if not self.equipos:
            return ["No hay equipos registrados."]
        salida = []
        for equipo in self.equipos.values():
            estado = "Disponible" if equipo.disponible else "Prestado"
            salida.append(f"{equipo.nombre} ({equipo.categoria}) - {estado}")
        return salida

    def consultar_prestamos(self):
        if not self.prestamos:
            return ["No hay prestamos registrados."]
        salida = []
        for idx, prestamo in enumerate(self.prestamos, start=1):
            salida.append(
                f"{idx}. Equipo: {prestamo.equipo.nombre} | "
                f"Usuario: {prestamo.usuario.nombre} ({prestamo.usuario.documento}) | "
                f"Inicio: {prestamo.fecha_prestamo} | "
                f"Estado: {prestamo.estado} | "
                f"Devolucion: {prestamo.fecha_devolucion or '-'}"
            )
        return salida

    def cargar_datos_iniciales(self):
        self.registrar_equipo("Laptop Dell", "Computo")
        self.registrar_equipo("Proyector Epson", "Audiovisual")
        self.registrar_equipo("Tablet Samsung", "Movil")
        self.registrar_usuario("1001", "Ana")
        self.registrar_usuario("1002", "Carlos")


def mostrar_menu():
    print("\n=== SISTEMA DE PRESTAMOS DE EQUIPOS ===")
    print("1. Registrar equipo")
    print("2. Registrar usuario")
    print("3. Registrar prestamo")
    print("4. Devolver equipo")
    print("5. Consultar equipos")
    print("6. Consultar prestamos")
    print("7. Salir")


def main():
    sistema = SistemaPrestamos()
    sistema.cargar_datos_iniciales()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion (1-7): ").strip()

        if opcion == "1":
            nombre = input("Nombre del equipo: ").strip()
            categoria = input("Categoria: ").strip()
            ok, mensaje = sistema.registrar_equipo(nombre, categoria)
            print(("OK: " if ok else "ERROR: ") + mensaje)
        elif opcion == "2":
            documento = input("Documento del usuario: ").strip()
            nombre = input("Nombre del usuario: ").strip()
            ok, mensaje = sistema.registrar_usuario(documento, nombre)
            print(("OK: " if ok else "ERROR: ") + mensaje)
        elif opcion == "3":
            equipo = input("Nombre exacto del equipo: ").strip()
            documento = input("Documento del usuario: ").strip()
            ok, mensaje = sistema.registrar_prestamo(equipo, documento)
            print(("OK: " if ok else "ERROR: ") + mensaje)
        elif opcion == "4":
            equipo = input("Nombre exacto del equipo a devolver: ").strip()
            ok, mensaje = sistema.devolver_prestamo(equipo)
            print(("OK: " if ok else "ERROR: ") + mensaje)
        elif opcion == "5":
            print("\n--- Equipos ---")
            for linea in sistema.consultar_equipos():
                print(linea)
        elif opcion == "6":
            print("\n--- Prestamos ---")
            for linea in sistema.consultar_prestamos():
                print(linea)
        elif opcion == "7":
            print("Saliendo del sistema. Hasta pronto.")
            break
        else:
            print("Opcion invalida, intenta de nuevo.")


if __name__ == "__main__":
    main()