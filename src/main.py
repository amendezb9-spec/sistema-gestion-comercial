from ast import While

import productos
import ventas
import inventario
import reportes


def main():
    while True:
        print("\n==== SISTEMA DE GESTIÓN COMERCIAL ==== ")
        print("1.  Gestion de Productos")
        print("2.  Resgistro de Ventas")
        print("3.  Control de INVENTARIOS")
        print("4.  Reporte y Estadisticas")
        print("0.  Salir")
        
        opcion = input("Seleccione una opcion:  ")
        
        if opcion == "1":
            productos.menu()
            
        elif opcion == "2":
            ventas.menu()
            
        elif opcion =="3":
            inventario.menu()
            
        elif opcion == "4":
            reportes.menu()
            
        elif opcion == "0":
            print("Gracias por utilizar el sistema.")
            break
        
        else:
            print("opcion invalida. intente nuevamente.")
            
if __name__ == "__main__":
    main()