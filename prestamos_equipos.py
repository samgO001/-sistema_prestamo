# ============================================================
# Sistema de Préstamos de Equipos
# Proyecto de clase - Estructuras de datos en Python
# ============================================================

from datetime import date

equipos = {
    "Laptop Dell": {
        "disponible": True,
        "prestamos": []
    },
    "Laptop HP": {
        "disponible": True,
        "prestamos": []
    },
    "Proyector Epson": {
        "disponible": True,
        "prestamos": []
    },
    "Tablet Samsung": {
        "disponible": True,
        "prestamos": []
    },
    "Cámara Canon": {
        "disponible": True,
        "prestamos": []
    }
}

def mostrar_equipos():
    print("\n" + "=" * 45)
    print("       INVENTARIO DE EQUIPOS")
    print("=" * 45)
    
    for nombre, datos in equipos.items():
        if datos["disponible"]:
            estado = "Disponible"
        else:
            estado = "Prestado"
        
        print(f"  {nombre:<20} {estado}")
    
    print("=" * 45)

# Línea de prueba temporal

# ── Función 2: Registrar un nuevo préstamo ───────────────────
def registrar_prestamo():
    print("\n" + "=" * 45)
    print("       REGISTRAR PRÉSTAMO")
    print("=" * 45)

    # Muestra los equipos disponibles
    mostrar_equipos()

    # Solicita el nombre del equipo
    nombre_equipo = input("\n¿Qué equipo desea prestar? (escribe el nombre exacto): ")

    # Valida que el equipo exista
    if nombre_equipo not in equipos:
        print(f"\nEl equipo '{nombre_equipo}' no existe en el sistema.")
        return

    # Valida que el equipo esté disponible
    if not equipos[nombre_equipo]["disponible"]:
        print(f"\nEl equipo '{nombre_equipo}' ya está prestado.")
        return

    # Solicita el nombre del usuario
    nombre_usuario = input("¿Nombre del usuario que lo toma prestado?: ")

    # Crea una tupla inmutable con (usuario, fecha)
    fecha_hoy = str(date.today())
    prestamo = (nombre_usuario, fecha_hoy)

    # Guarda la tupla en la lista de préstamos del equipo
    equipos[nombre_equipo]["prestamos"].append(prestamo)

    # Marca el equipo como no disponible
    equipos[nombre_equipo]["disponible"] = False

    print(f"\nPréstamo registrado exitosamente.")
    print(f"   Equipo  : {nombre_equipo}")
    print(f"   Usuario : {nombre_usuario}")
    print(f"   Fecha   : {fecha_hoy}")

    # ── Función 3: Devolver un equipo prestado ───────────────────
def devolver_equipo():
    print("\n" + "=" * 45)
    print("         DEVOLVER EQUIPO")
    print("=" * 45)

    # Muestra el estado actual de los equipos
    mostrar_equipos()

    # Solicita el nombre del equipo a devolver
    nombre_equipo = input("\n¿Qué equipo desea devolver? (escribe el nombre exacto): ")

    # Valida que el equipo exista
    if nombre_equipo not in equipos:
        print(f"\nEl equipo '{nombre_equipo}' no existe en el sistema.")
        return

    # Valida que el equipo esté efectivamente prestado
    if equipos[nombre_equipo]["disponible"]:
        print(f"\nEl equipo '{nombre_equipo}' no está prestado actualmente.")
        return

    # Marca el equipo como disponible nuevamente
    equipos[nombre_equipo]["disponible"] = True

    print(f"\nEl equipo '{nombre_equipo}' fue devuelto exitosamente.")
    print(f"   Ya está disponible para un nuevo préstamo.")


    # ── Función 4: Ver historial completo de préstamos ───────────
def ver_historial():
    print("\n" + "=" * 45)
    print("      HISTORIAL DE PRÉSTAMOS")
    print("=" * 45)

    for nombre, datos in equipos.items():
        print(f"\n{nombre}:")

        # Verifica si el equipo tiene préstamos registrados
        if len(datos["prestamos"]) == 0:
            print("     Sin préstamos registrados.")
        else:
            # Recorre la lista de tuplas (usuario, fecha)
            for i, prestamo in enumerate(datos["prestamos"], start=1):
                usuario = prestamo[0]   # primer elemento de la tupla
                fecha   = prestamo[1]   # segundo elemento de la tupla
                print(f"     {i}. Usuario: {usuario} — Fecha: {fecha}")

    print("\n" + "=" * 45)


    # ── Función 5: Agregar un nuevo equipo al sistema ────────────
def agregar_equipo():
    print("\n" + "=" * 45)
    print("        AGREGAR NUEVO EQUIPO")
    print("=" * 45)

    # Muestra los equipos actuales
    mostrar_equipos()

    # Solicita el nombre del nuevo equipo
    nombre_equipo = input("\n¿Nombre del nuevo equipo a agregar?: ")

    # Verifica que el equipo no exista ya en el diccionario
    if nombre_equipo in equipos:
        print(f"\nEl equipo '{nombre_equipo}' ya está registrado en el sistema.")
        return

    # Agrega el nuevo equipo al diccionario con estado disponible
    equipos[nombre_equipo] = {
        "disponible": True,
        "prestamos": []
    }

    print(f"\nEl equipo '{nombre_equipo}' fue agregado exitosamente.")
    print(f"   Estado: Disponible")

    # ── Función 6: Menú principal interactivo ────────────────────
def menu():
    print("\n" + "=" * 45)
    print("   SISTEMA DE PRÉSTAMOS DE EQUIPOS")
    print("=" * 45)

    while True:
        # Muestra las opciones disponibles
        print("\n¿Qué deseas hacer?")
        print("  1. Ver equipos disponibles")
        print("  2. Registrar préstamo")
        print("  3. Devolver equipo")
        print("  4. Ver historial de préstamos")
        print("  5. Agregar nuevo equipo")
        print("  6. Salir")
        print("-" * 45)

        # Solicita la opción al usuario
        opcion = input("Selecciona una opción (1-6): ")

        # Ejecuta la función según la opción elegida
        if opcion == "1":
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            print("\n¡Hasta luego! Cerrando el sistema...")
            break
        else:
            print("\nOpción inválida. Por favor elige un número del 1 al 6.")

# ── Punto de entrada del programa ────────────────────────────

menu()