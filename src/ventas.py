
# MODULO 3 - REGISTRO DE VENTAS

import json
from datetime import datetime
from pathlib import Path
from decimal import Decimal

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
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with open(ARCHIVO_VENTAS, "w", encoding="utf-8") as archivo:
        json.dump(ventas, archivo, indent=4, ensure_ascii=False)


# Registrar venta
def registrar_venta():
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

        ventas.append(nueva_venta)

        # Guardar la venta antes de actualizar inventario
        guardar_ventas(ventas)

        producto["cantidad"] = disponible - cantidad
        guardar_productos(productos)

        print("\nVenta registrada correctamente.")
        print("Producto:", producto["nombre"])
        print("Cantidad vendida:", cantidad)
        print(f"Total: Q{total:.2f}")
        print("Stock restante:", producto["cantidad"])

        if producto["cantidad"] <= int(producto["stock_minimo"]):
            print("ALERTA: Stock bajo.")

    except (ValueError, TypeError, KeyError):
        print("Error: verifique los datos ingresados.")
    except (OSError, json.JSONDecodeError) as error:
        print("Error al guardar o leer datos:", error)


# Mostrar ventas
def mostrar_ventas():
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
        print(f"Total: Q{venta['total']:.2f}")


# Estadisticas de ventas
def estadisticas_ventas():
    print("\n===== ESTADISTICAS DE VENTAS =====")

    ventas = cargar_ventas()

    if not ventas:
        print("No hay ventas registradas.")
        return

    totales = [venta["total"] for venta in ventas]

    print(f"Total vendido: Q{sum(totales):.2f}")
    print(f"Promedio: Q{sum(totales) / len(totales):.2f}")
    print(f"Venta mas alta: Q{max(totales):.2f}")
    print(f"Venta mas baja: Q{min(totales):.2f}")

    try:
        umbral = float(input("Ingrese el monto para comparar: Q"))

        if umbral < 0:
            print("El monto no puede ser negativo.")
            return

        cantidad = sum(1 for total in totales if total > umbral)

        print("Ventas mayores al monto:", cantidad)

    except ValueError:
        print("Ingrese un monto valido.")


# Menu de ventas
def menu():
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
                break

            else:
                print("Opcion invalida. Intente nuevamente.")

        except (OSError, ValueError, json.JSONDecodeError) as error:
            print("No se pudo completar la operacion:", error)


if __name__ == "__main__":
    menu()
