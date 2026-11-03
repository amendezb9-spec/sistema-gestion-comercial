
# MODULO 2 - CONTROL DE INVENTARIO

from productos import cargar_productos, guardar_productos, buscar_producto


# Registrar entrada de productos
def registrar_entrada():
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
        cantidad = int(input("Cantidad a ingresar: "))

        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            return

        producto["cantidad"] += cantidad
        guardar_productos(productos)

        print("Entrada registrada correctamente.")
        print("Cantidad actual:", producto["cantidad"])

    except ValueError:
        print("Ingrese una cantidad valida.")


# Registrar salida de productos
def registrar_salida():
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
        cantidad = int(input("Cantidad a retirar: "))

        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            return

        if cantidad > producto["cantidad"]:
            print("No hay suficientes productos.")
            return

        producto["cantidad"] -= cantidad
        guardar_productos(productos)

        print("Salida registrada correctamente.")
        print("Cantidad actual:", producto["cantidad"])

        if producto["cantidad"] <= producto["stock_minimo"]:
            print("ALERTA: Stock bajo.")

    except ValueError:
        print("Ingrese una cantidad valida.")


# Consultar inventario
def consultar_inventario():
    productos = cargar_productos()

    print("\n===== INVENTARIO ACTUAL =====")

    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        if not producto.get("activo", True):
            continue

        print("--------------------------")
        print("Codigo:", producto["codigo"])
        print("Nombre:", producto["nombre"])
        print("Cantidad:", producto["cantidad"])
        print("Stock minimo:", producto["stock_minimo"])


# Alertas de stock
def alertas_stock():
    productos = cargar_productos()
    encontrados = False

    print("\n===== ALERTAS DE STOCK =====")

    for producto in productos:
        if not producto.get("activo", True):
            continue

        if producto["cantidad"] <= producto["stock_minimo"]:
            encontrados = True

            print("--------------------------")
            print("Producto:", producto["nombre"])
            print("Codigo:", producto["codigo"])
            print("Cantidad:", producto["cantidad"])
            print("Stock minimo:", producto["stock_minimo"])

    if not encontrados:
        print("No hay productos con stock bajo.")


# Menu principal de inventario
def menu():
    while True:
        print("\n===== CONTROL DE INVENTARIO =====")
        print("1. Registrar entrada")
        print("2. Registrar salida")
        print("3. Consultar inventario")
        print("4. Alertas de stock")
        print("0. Regresar al menu principal")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_entrada()

        elif opcion == "2":
            registrar_salida()

        elif opcion == "3":
            consultar_inventario()

        elif opcion == "4":
            alertas_stock()

        elif opcion == "0":
            break

        else:
            print("Opcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
