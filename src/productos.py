# Lista global para almacenar los productos en memoria
import json 
import math  
from pathlib import Path 

# Ubicacion de la carpeta principal del proyecto 
BASE_DIR = Path (__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" 
ARCHIVO_PRODUCTOS = DATA_DIR / "productos.json" 

#==========================================================
# Guardar y cargar productos 
#==========================================================
def guardar_productos(productos): 
    DATA_DIR.mkdir(parents=True, exist_ok=True) 

    with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as archivo: 
        json.dump(productos, archivo, indent=4, ensure_ascii=False) 


def cargar_productos():
    DATA_DIR.mkdir(parents=True, exist_ok=True)  

    if not ARCHIVO_PRODUCTOS.exists(): 
        guardar_productos([])
        return []

    try: 
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo: 
            datos = json.load(archivo) 


        if not isinstance(datos, list): 
            raise ValueError("El archivo debe contener una lista.") 

        return datos 

    except (json.JSONDecodeError, ValueError) as error: 
        raise RuntimeError( 
            f"No se pudo leer productos.json: {error}" 
        ) from error 
    

#==============================================================
#  Buscar producto por codigo 
# =============================================================



def buscar_producto(productos, codigo):
    codigo = str(codigo).strip().upper()

    for producto in productos:
        if not isinstance(producto, dict):
            continue

        codigo_guardado = str(producto.get("codigo", "")).strip().upper()

        if codigo_guardado == codigo:
            return producto

    return None


#==============================================================
# Validar Precios y Cantidades 
#==============================================================

def leer_numero(mensaje,tipo=float): 
    while True: 

        try: 
            valor = tipo(input(mensaje)) 

            if valor < 0: 
                print("Error: no se permiten valores negativos. intente nuevamente.")
                continue 

            if tipo == float and not math.isfinite(valor): 
                print("Error: ingrese un numero valido. intente nuevamente.")
                continue 

            return valor 
        except ValueError: 
            print("Error: debe ingresar un numero valido") 
            
            
            



#==============================================================
# Registrar Producto 
#==============================================================

def registrar_producto():  
    productos = cargar_productos() 
    print("DEBUG - Productos cargados:", productos)  
        

    print("\n--- Registrar Producto ---") 

    codigo = input("Ingrese el codigo:").strip().upper()

    if not codigo: 
        print("Error: el codigo no puede estar vacio")
        return 
    print("DEBUG - Codigo ingresado:", repr(codigo)) 
    print("DEBUG - Resultado busqueda:", buscar_producto(productos, codigo)) 

    if buscar_producto(productos, codigo) is not None: 
        print(f"Error: ya existe un producto con ese codigo.")
        return 
    
    nombre = input("Ingrese el nombre:").strip()
    categoria = input("Ingrese la categoria: ").strip()

    if not nombre or not categoria:
        print("Error: nombre y categoria son obligatorios.")
        return 

    precio = leer_numero("Ingrese el precio Q: ", float)
    cantidad = leer_numero("Ingrese la cantidad disponible: ", int) 
    stock_minimo = leer_numero("Ingrese el stock minimo: ", int) 

    nuevo_producto = { 
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria, 
        "precio": precio,
        "cantidad": cantidad, 
        "stock_minimo": stock_minimo,
        "activo": True 
    }

    productos.append(nuevo_producto)
    guardar_productos(productos) 

    print(f"Productos '{nombre}' registrado exitosamente.")


def listar_productos(): 
    productos = cargar_productos()  

    print("\n===== LISTA DE PRODUCTOS =====")

    if not productos: 
        print("No hay productos registrados.") 
        return 

    for producto in productos: 
        print(f"Codigo: {producto.get('codigo')}") 
        print(f"Nombre: {producto.get('nombre')}") 
        print("------------------------")

    # Nuevo menu 
def menu(): 
        while True: 
            print("\n=====Gestion de productos=====")
            print("1. Registrar producttos")
            print("2. Consultar productos") 
            print("3. Lista de productos") 
            print("4. Modificar producto") 
            print("5. Desactivar producto")
            print("0. Regresar al menu principal") 

            opcion = input("Seleccione una opcion: ").strip()
            print("DEBUG - Opción recibida:", repr(opcion))


            if opcion == "1": 
                registrar_producto() 
            
            elif opcion == "0": 
                break      
            elif opcion == "3": 
                listar_productos()

            elif opcion in ("2", "4", "5"): 
                print("Opcion pendiente de implementacion.") 

            else: 
                print("Opcion invalida.")

if __name__ == "__main__":
    menu() 