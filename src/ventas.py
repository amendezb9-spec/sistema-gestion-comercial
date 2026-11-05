
"""Modulo 3: Registro de ventas del sistema comercial."""

import json
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

from productos import (
    cargar_productos,
    guardar_productos,
    buscar_producto
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
ARCHIVO_VENTAS = DATA_DIR / "ventas.json"


# Cargar ventas guardadas
def cargar_ventas():
    """Carga las ventas almacenadas en el archivo JSON."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not ARCHIVO_VENTAS.exists():
        return []

    with open(ARCHIVO_VENTAS, "r", encoding="utf-8") as archivo:
        ventas = json.load(archivo)

    if not isinstance(ventas, list):
        raise ValueError("El archivo de ventas no es valido.")

    return ventas


# Guardar ventas
def guardar_ventas(ventas):
    """Guarda las ventas registradas en un archivo JSON."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with open(ARCHIVO_VENTAS, "w", encoding="utf-8") as archivo:
        json.dump(ventas, archivo, indent=4, ensure_ascii=False)


# Registrar venta
def registrar_venta():
    """Registra una venta y actualiza el inventario."""
    print("\n===== REGISTRAR VENTA =====")

    productos = cargar_productos()
    codigo = input("Codigo del producto: ").strip().upper()
    producto = buscar_producto(productos, codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    if not producto.get("activo", True):
        print("El producto esta desactivado.")
        return

    try:
        cantidad = int(input("Cantidad a vender: "))

        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            return

        disponible = int(producto["cantidad"])

        if cantidad > disponible:
            print("No hay suficientes productos.")
            print("Cantidad disponible:", disponible)
            return

        precio = Decimal(str(producto["precio"]))

        if not precio.is_finite() or precio < 0:
            print("El precio no es valido.")
            return

        total = precio * cantidad
        ventas = cargar_ventas()

        nueva_venta = {
            "codigo": codigo,
            "producto": producto["nombre"],
            "cantidad": cantidad,
            "precio": float(precio),
            "total": float(total),
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Actualizar inventario
        producto["cantidad"] = disponible - cantidad
        guardar_productos(productos)

        # Guardar la venta
        ventas.append(nueva_venta)

        try:
            guardar_ventas(ventas)
        except OSError:
            producto["cantidad"] = disponible
            guardar_productos(productos)
            raise

        print("\nVenta registrada correctamente.")
        print("Producto:", producto["nombre"])
        print("Cantidad vendida:", cantidad)
        print(f"Total: Q{total:.2f}")
        print("Stock restante:", producto["cantidad"])

        if producto["cantidad"] <= int(producto["stock_minimo"]):
            print("ALERTA: Stock bajo.")

    except (ValueError, TypeError, KeyError, InvalidOperation):
        print("Error: verifique los datos ingresados.")

    except OSError as error:
        print("Error al guardar o leer datos:", error)


# Mostrar ventas
def mostrar_ventas():
    """Muestra todas las ventas registradas."""
    print("\n===== LISTADO DE VENTAS =====")

    ventas = cargar_ventas()

    if not ventas:
        print("No hay ventas registradas.")
        return

    for numero, venta in enumerate(ventas, start=1):
        print("\nVenta:", numero)
        print("Fecha:", venta["fecha"])
        print("Producto:", venta["producto"])
        print("Cantidad:", venta["cantidad"])
        print(f"Total: Q{Decimal(str(venta['total'])):.2f}")


# Estadisticas de ventas
def estadisticas_ventas():
    """Calcula el total, promedio y estadisticas de ventas."""
    print("\n===== ESTADISTICAS DE VENTAS =====")

    ventas = cargar_ventas()

    if not ventas:
        print("No hay ventas registradas.")
        return

    totales = [
        Decimal(str(venta["total"]))
        for venta in ventas
    ]

    total_general = sum(totales, Decimal("0.00"))

    print(f"Total vendido: Q{total_general:.2f}")
    print(f"Promedio: Q{total_general / len(totales):.2f}")
    print(f"Venta mas alta: Q{max(totales):.2f}")
    print(f"Venta mas baja: Q{min(totales):.2f}")

    try:
        umbral = Decimal(
            input("Ingrese el monto para comparar: Q").strip()
        )

        if not umbral.is_finite() or umbral < 0:
            print("Ingrese un monto valido no negativo.")
            return

        cantidad = sum(
            1 for total in totales if total > umbral
        )

        print("Ventas mayores al monto:", cantidad)

    except InvalidOperation:
        print("Ingrese un monto valido.")


# Menu de ventas
def menu():
    """Muestra las opciones del modulo de ventas."""
    while True:
        print("\n===== REGISTRO DE VENTAS =====")
        print("1. Registrar venta")
        print("2. Mostrar ventas")
        print("3. Estadisticas de ventas")
        print("0. Regresar al menu principal")

        opcion = input("Seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                registrar_venta()

            elif opcion == "2":
                mostrar_ventas()

            elif opcion == "3":
                estadisticas_ventas()

            elif opcion == "0":
                print("Regresando al menu principal...")
                break

            else:
                print("Opcion invalida. Intente nuevamente.")

        except (OSError, ValueError, KeyError, TypeError) as error:
            print("No se pudo completar la operacion:", error)


if __name__ == "__main__":
    menu()
