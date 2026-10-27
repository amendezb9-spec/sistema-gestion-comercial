# Lista global para almacenar los productos en memoria
productos = []

def registrar_producto():
  print(" REGISTRAR NUEVO PRODUCTO ")
  codigo = input("Ingrese el código del producto: ").strip()

  # Validar que el código no esté duplicado
  for p in productos:
    if p["codigo"] == codigo:
      print("¡Error! Ya existe un producto registrado con ese código.")
      return

  nombre = input("Ingrese el nombre del producto: ").strip()
  categoria = input("Ingrese la categoría: ").strip()

  # Validar precio de venta (debe ser numérico y positivo)
  try:
    precio = float(input("Ingrese el precio de venta: "))
    if precio < 0:
      print("¡Error! El precio no puede ser negativo.")
      return
  except ValueError:
    print("¡Error! Debe ingresar un valor numérico válido para el precio.")
    return

  # Validar cantidad disponible (debe ser entero y positivo)
  try:
    cantidad = int(input("Ingrese la cantidad disponible: "))
    if cantidad < 0:
      print("¡Error! La cantidad no puede ser negativa.")
      return
  except ValueError:
    print("¡Error! Debe ingresar un número entero válido para la cantidad.")
    return

  # Validar stock mínimo (debe ser entero y positivo)
  try:
    stock_minimo = int(input("Ingrese el stock mínimo: "))
    if stock_minimo < 0:
      print("¡Error! El stock mínimo no puede ser negativo.")
      return
  except ValueError:
    print("¡Error! Debe ingresar un número entero válido para el stock mínimo.")
    return

  # Crear el diccionario del producto y agregarlo a la lista
  nuevo_producto = {
      "codigo": codigo,
      "nombre": nombre,
      "categoria": categoria,
      "precio": precio,
      "cantidad": cantidad,
      "stock_minimo": stock_minimo,
      "activo": True,  # True para activo, False para desactivado
  }

  productos.append(nuevo_producto)
  print(f"¡Éxito! El producto '{nombre}' se ha registrado correctamente.")

def mostrar_productos():
  print("\n--- LISTADO DE PRODUCTOS ---")
  if not productos:
    print("No hay productos registrados todavía.")
    return
*
  for p in productos:
    estado = "Activo" if p["activo"] else "Desactivado"
    print(
        f"Código: {p['codigo']} | Nombre: {p['nombre']} | Categoría:"
        f" {p['categoria']} | Precio: Q{p['precio']:.2f} | Stock:"
        f" {p['cantidad']} (Mín: {p['stock_minimo']}) | Estado: {estado}"
    )
