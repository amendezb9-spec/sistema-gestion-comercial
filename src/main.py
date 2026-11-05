
"""Menu principal del Sistema de Gestion Comercial."""

import productos
import ventas
import inventario
import reportes


def main():
    """Mostrar el menu principal y ejecutar sus opciones."""

    while True:
        print("\n===== SISTEMA DE GESTION COMERCIAL =====")
        print("1. Gestion de Productos")
        print("2. Registro de Ventas")
        print("3. Control de Inventarios")
        print("4. Reportes y Estadisticas")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            productos.menu()

        elif opcion == "2":
            ventas.menu()

        elif opcion == "3":
            inventario.menu()

        elif opcion == "4":
            reportes.menu()

        elif opcion == "0":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    main()
