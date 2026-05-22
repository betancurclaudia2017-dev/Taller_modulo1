# Taller Modulo 3
# Sistema de Gestion de una Tienda de Videojuegos

MENU = """
===== TIENDA DE VIDEOJUEGOS =====
1. Agregar videojuego
2. Mostrar inventario
3. Buscar videojuego por codigo
4. Actualizar precio
5. Registrar venta
6. Mostrar estadisticas
7. Eliminar videojuego
8. Salir
"""

PLATAFORMAS = ["PC", "PlayStation", "Xbox", "Nintendo"]

videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}


def formatear_precio(valor):
    return "$" + format(valor, ",.0f").replace(",", ".")


def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto != "":
            return texto

        print("Error: el campo no puede estar vacio.")


def pedir_numero_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero > 0:
                return numero

            print("Error: el numero debe ser mayor que cero.")
        except ValueError:
            print("Error: debes ingresar un numero valido.")


def pedir_plataforma():
    print("\nSeleccione la plataforma:")

    for indice, plataforma in enumerate(PLATAFORMAS, start=1):
        print(f"{indice}. {plataforma}")

    while True:
        try:
            opcion = int(input("Ingrese el numero de la plataforma: "))

            if 1 <= opcion <= len(PLATAFORMAS):
                return PLATAFORMAS[opcion - 1]

            print("Error: selecciona una opcion valida.")
        except ValueError:
            print("Error: debes ingresar un numero valido.")


def agregar_videojuego(videojuegos):
    print("\n--- AGREGAR VIDEOJUEGO ---")

    codigo = pedir_texto("Ingrese el codigo del videojuego: ").upper()

    if codigo in videojuegos:
        print("Error: ya existe un videojuego con ese codigo.")
        return

    nombre = pedir_texto("Ingrese el nombre del videojuego: ")
    plataforma = pedir_plataforma()
    precio = pedir_numero_entero("Ingrese el precio del videojuego: ")
    cantidad = pedir_numero_entero("Ingrese la cantidad en inventario: ")

    videojuegos[codigo] = {
        "nombre": nombre,
        "plataforma": plataforma,
        "precio": precio,
        "cantidad": cantidad
    }

    print("Videojuego agregado correctamente.")


def mostrar_inventario(videojuegos):
    print("\n--- INVENTARIO DE VIDEOJUEGOS ---")

    if not videojuegos:
        print("No hay videojuegos registrados.")
        return

    for codigo, videojuego in videojuegos.items():
        print(f"\nCodigo: {codigo}")
        print(f"Nombre: {videojuego['nombre']}")
        print(f"Plataforma: {videojuego['plataforma']}")
        print(f"Precio: {formatear_precio(videojuego['precio'])}")
        print(f"Cantidad: {videojuego['cantidad']}")


def buscar_videojuego(videojuegos):
    print("\n--- BUSCAR VIDEOJUEGO ---")

    codigo = pedir_texto("Ingrese el codigo del videojuego en COP: ").upper()

    if codigo not in videojuegos:
        print("No existe un videojuego con ese codigo.")
        return

    videojuego = videojuegos[codigo]

    print("\nVideojuego encontrado:")
    print(f"Codigo: {codigo}")
    print(f"Nombre: {videojuego['nombre']}")
    print(f"Plataforma: {videojuego['plataforma']}")
    print(f"Precio: {formatear_precio(videojuego['precio'])}")
    print(f"Cantidad: {videojuego['cantidad']}")


def actualizar_precio(videojuegos):
    print("\n--- ACTUALIZAR PRECIO ---")

    codigo = pedir_texto("Ingrese el codigo del videojuego: ").upper()

    if codigo not in videojuegos:
        print("No existe un videojuego con ese codigo.")
        return

    precio_nuevo = pedir_numero_entero("Ingrese el nuevo precio: ")
    videojuegos[codigo]["precio"] = precio_nuevo

    print("Precio actualizado correctamente.")


def registrar_venta(videojuegos):
    print("\n--- REGISTRAR VENTA ---")

    codigo = pedir_texto("Ingrese codigo del videojuego: ").upper()

    if codigo not in videojuegos:
        print("No existe un videojuego con ese codigo.")
        return

    cantidad_vender = pedir_numero_entero("Ingrese cantidad a vender: ")
    videojuego = videojuegos[codigo]

    if cantidad_vender > videojuego["cantidad"]:
        print("No hay suficiente inventario para realizar la venta.")
        print(f"Cantidad disponible: {videojuego['cantidad']}")
        return

    total = videojuego["precio"] * cantidad_vender
    videojuego["cantidad"] -= cantidad_vender

    print("\nFactura:")
    print(f"Juego: {videojuego['nombre']}")
    print(f"Precio unitario: {formatear_precio(videojuego['precio'])}")
    print(f"Cantidad: {cantidad_vender}")
    print(f"Total: {formatear_precio(total)}")
    print("Venta registrada correctamente.")


def mostrar_estadisticas(videojuegos):
    print("\n--- ESTADISTICAS ---")

    if not videojuegos:
        print("No hay videojuegos registrados para calcular estadisticas.")
        return

    total_videojuegos = len(videojuegos)
    valor_total_inventario = 0
    suma_precios = 0

    codigo_mas_costoso = None
    codigo_mayor_cantidad = None

    for codigo, videojuego in videojuegos.items():
        valor_total_inventario += videojuego["precio"] * videojuego["cantidad"]
        suma_precios += videojuego["precio"]

        if codigo_mas_costoso is None or videojuego["precio"] > videojuegos[codigo_mas_costoso]["precio"]:
            codigo_mas_costoso = codigo

        if codigo_mayor_cantidad is None or videojuego["cantidad"] > videojuegos[codigo_mayor_cantidad]["cantidad"]:
            codigo_mayor_cantidad = codigo

    promedio_precios = suma_precios / total_videojuegos
    videojuego_mas_costoso = videojuegos[codigo_mas_costoso]
    videojuego_mayor_cantidad = videojuegos[codigo_mayor_cantidad]

    print(f"Total de videojuegos registrados: {total_videojuegos}")
    print(f"Valor total del inventario: {formatear_precio(valor_total_inventario)}")
    print(f"Videojuego mas costoso: {videojuego_mas_costoso['nombre']} ({formatear_precio(videojuego_mas_costoso['precio'])})")
    print(f"Videojuego con mayor cantidad disponible: {videojuego_mayor_cantidad['nombre']} ({videojuego_mayor_cantidad['cantidad']} unidades)")
    print(f"Promedio de precios: {formatear_precio(promedio_precios)}")


def eliminar_videojuego(videojuegos):
    print("\n--- ELIMINAR VIDEOJUEGO ---")

    codigo = pedir_texto("Ingrese el codigo del videojuego: ").upper()

    if codigo not in videojuegos:
        print("No existe un videojuego con ese codigo.")
        return

    videojuego = videojuegos[codigo]
    del videojuegos[codigo]

    print(f"El videojuego '{videojuego['nombre']}' fue eliminado correctamente.")


def menu():
    while True:
        print(MENU)
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            agregar_videojuego(videojuegos)
        elif opcion == "2":
            mostrar_inventario(videojuegos)
        elif opcion == "3":
            buscar_videojuego(videojuegos)
        elif opcion == "4":
            actualizar_precio(videojuegos)
        elif opcion == "5":
            registrar_venta(videojuegos)
        elif opcion == "6":
            mostrar_estadisticas(videojuegos)
        elif opcion == "7":
            eliminar_videojuego(videojuegos)
        elif opcion == "8":
            print("Gracias por usar el sistema. Hasta pronto.")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
