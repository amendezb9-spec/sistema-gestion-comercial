
# MODULO 4 - REPORTES Y ESTADISTICAS

from decimal import Decimal, InvalidOperation
from productos import cargar_productos
from ventas import cargar_ventas


# Reporte de productos
def reporte_productos():
    productos = cargar_productos()

    print("\n===== REPORTE DE PRODUCTOS =====")

    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        print("--------------------------")
        print("Codigo:", producto["codigo"])
        print("Nombre:", producto["nombre"])
        print("Categoria:", producto["categoria"])
        print("Precio: Q", producto["precio"])
        print("Cantidad:", producto["cantidad"])
        print("Estado:", "Activo" if producto.get("activo", True)
              else "Inactivo")


# Reporte de inventario bajo
def reporte_stock_bajo():
    productos = cargar_productos()
    encontrados = False

    print("\n===== PRODUCTOS CON STOCK BAJO =====")

    for producto in productos:
        if not producto.get("activo", True):
            continue

        try:
            cantidad = int(producto["cantidad"])
            minimo = int(producto["stock_minimo"])
        except (ValueError, TypeError, KeyError):
            print("Hay un producto con datos invalidos.")
            continue

        if cantidad <= minimo:
            encontrados = True
            print("--------------------------")
            print("Codigo:", producto["codigo"])
            print("Producto:", producto["nombre"])
            print("Cantidad:", cantidad)
            print("Stock minimo:", minimo)

    if not encontrados:
        print("No hay productos con stock bajo.")


# Reporte general de ventas
def reporte_ventas():
    ventas = cargar_ventas()

    print("\n===== REPORTE DE VENTAS =====")

    if not ventas:
        print("No hay ventas registradas.")
        return

    total_general = Decimal("0.00")

    for numero, venta in enumerate(ventas, start=1):
        total = Decimal(str(venta["total"]))
        total_general += total

        print("--------------------------")
        print("Venta:", numero)
        print("Fecha:", venta["fecha"])
        print("Producto:", venta["producto"])
        print("Cantidad:", venta["cantidad"])
        print(f"Total: Q{total:.2f}")

    print("--------------------------")
    print(f"TOTAL GENERAL: Q{total_general:.2f}")


# Estadisticas de ventas
def estadisticas():
    ventas = cargar_ventas()

    print("\n===== ESTADISTICAS GENERALES =====")

    if not ventas:
        print("No hay ventas registradas.")
        return

    totales = [Decimal(str(v["total"])) for v in ventas]

    total = sum(totales)
    promedio = total / len(totales)

    print("Cantidad de ventas:", len(ventas))
    print(f"Total vendido: Q{total:.2f}")
    print(f"Promedio por venta: Q{promedio:.2f}")
    print(f"Venta mas alta: Q{max(totales):.2f}")
    print(f"Venta mas baja: Q{min(totales):.2f}")

    try:
        monto = Decimal(
            input("Ingrese el monto a comparar: Q").strip()
        )

        if not monto.is_finite() or monto < 0:
            print("El monto debe ser un numero no negativo.")
            return

        cantidad = sum(1 for venta in totales if venta > monto)

        print("Ventas mayores al monto:", cantidad)

    except InvalidOperation:
        print("Ingrese un monto valido.")


# Resumen general del negocio
def resumen_general():
    productos = cargar_productos()
    ventas = cargar_ventas()

    activos = [
        p for p in productos
        if p.get("activo", True)
    ]

    total_ventas = sum(
        (Decimal(str(v["total"])) for v in ventas),
        Decimal("0.00")
    )

    print("\n===== RESUMEN GENERAL =====")
    print("Productos registrados:", len(productos))
    print("Productos activos:", len(activos))
    print("Ventas realizadas:", len(ventas))
    print(f"Dinero vendido: Q{total_ventas:.2f}")


# Menu de reportes
def menu():
    while True:
        print("\n===== REPORTES Y ESTADISTICAS =====")
        print("1. Reporte de productos")
        print("2. Reporte de stock bajo")
        print("3. Reporte de ventas")
        print("4. Estadisticas de ventas")
        print("5. Resumen general")
        print("0. Regresar al menu principal")

        opcion = input("Seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                reporte_productos()

            elif opcion == "2":
                reporte_stock_bajo()

            elif opcion == "3":
                reporte_ventas()

            elif opcion == "4":
                estadisticas()

            elif opcion == "5":
                resumen_general()

            elif opcion == "0":
                print("Regresando al menu principal...")
                break

            else:
                print("Opcion invalida. Intente nuevamente.")

        except (OSError, ValueError, KeyError, TypeError) as error:
            print("No se pudo generar el reporte:", error)


if __name__ == "__main__":
    menu()
