# Documento de Análisis de Procesos - Sistema de Gestión Comercial

## 1. Registro de Productos
* **Nombre del proceso:** Registro de Nuevos Productos.
* **Objetivo:** Dar de alta un nuevo producto en el sistema asegurando que cumpla con los parámetros comerciales requeridos.
* **Descripción del funcionamiento:** El sistema solicita el código, nombre, categoría, precio, cantidad inicial y stock mínimo. Valida que el código no exista previamente y que los valores numéricos no sean negativos.
* **Datos de entrada:** Código, nombre, categoría, precio, cantidad inicial, stock mínimo.
* **Procesamiento realizado:** Verificación de duplicidad en `productos.json`, validación de tipos de datos y rangos mayores o iguales a cero, creación del diccionario con estado activo en `True` y guardado en archivo.
* **Datos de salida:** Mensaje de éxito o error, actualización del archivo JSON.
* **Reglas de negocio:** No se permiten códigos duplicados ni precios/cantidades negativas.
* **Validaciones y posibles errores:** Ingresar letras en campos numéricos (ValueError), números negativos, códigos ya existentes.

## 2. Consulta y Modificación de Productos
* **Nombre del proceso:** Consulta y Modificación.
* **Objetivo:** Buscar la información detallada de un producto o actualizar sus atributos comerciales.
* **Descripción del funcionamiento:** Permite buscar por código exacto para visualizar los datos o modificarlos campo por campo (dejando el valor anterior si se presiona Enter sin escribir nada).
* **Datos de entrada:** Código del producto y nuevos valores opcionales.
* **Procesamiento realizado:** Búsqueda secuencial en la lista de productos cargados, sustitución de valores si son válidos, y persistencia de cambios.
* **Datos de salida:** Ficha del producto en pantalla o confirmación de modificación.
* **Reglas de negocio:** El código es inalterable una vez registrado; los nuevos valores numéricos no pueden ser negativos.
* **Validaciones y posibles errores:** Producto no encontrado, formato numérico incorrecto.

## 3. Registro de Ventas
* **Nombre del proceso:** Procesamiento de Venta al Cliente.
* **Objetivo:** Registrar la salida de mercancía, calcular subtotales, aplicar IVA (12%) y descontar existencias del inventario automáticamente.
* **Descripción del funcionamiento:** Se solicitan productos de forma repetitiva hasta ingresar 'fin'. Se valida stock disponible por cada línea de venta.
* **Datos de entrada:** Código de producto y cantidad a vender.
* **Procesamiento realizado:** Verificación de existencia y estado activo, validación de stock suficiente, cálculo de subtotal por producto, cálculo de IVA (12%) sobre el subtotal general, generación de número de venta consecutivo, descuento en inventario y registro en historial.
* **Datos de salida:** Factura detallada en consola y actualización de archivos de ventas, productos e inventario.
* **Reglas de negocio:** No se puede vender más de lo disponible en stock; el IVA aplicado es del 12%.
* **Validaciones y posibles errores:** Producto inexistente, cantidad solicitada mayor al inventario disponible, valores negativos o no numéricos.

## 4. Actualización de Inventario
* **Nombre del proceso:** Control de Movimientos de Inventario.
* **Objetivo:** Registrar entradas de mercancía y mantener una trazabilidad histórica de todos los movimientos.
* **Descripción del funcionamiento:** Se ingresa el código del producto, la cantidad a sumar por una nueva compra/entrada y una descripción opcional.
* **Datos de entrada:** Código de producto, cantidad de entrada, descripción.
* **Procesamiento realizado:** Búsqueda del producto, incremento de la cantidad disponible, creación de un registro de movimiento con fecha y hora actuales.
* **Datos de salida:** Mensaje de confirmación y registro guardado en `inventario.json`.
* **Reglas de negocio:** Las entradas deben incrementar el stock actual y registrarse con fecha y hora.
* **Validaciones y posibles errores:** Producto no encontrado, cantidad menor o igual a cero.

## 5. Lectura y Persistencia de Archivos
* **Nombre del proceso:** Gestión de Archivos JSON.
* **Objetivo:** Garantizar que los datos persistan entre ejecuciones del programa mediante archivos estructurados locales.
* **Descripción del funcionamiento:** Las funciones de lectura evalúan la existencia del archivo; si no existe, retornan una lista vacía. Las funciones de escritura serializan las estructuras en formato JSON legible.
* **Datos de entrada:** Nombre del archivo y estructuras de datos de Python (listas/diccionarios).
* **Procesamiento realizado:** Apertura de archivos usando codificación UTF-8, uso de `json.load()` y `json.dump()`.
* **Datos de salida:** Datos cargados en memoria o archivos actualizados en disco.
* **Reglas de negocio:** Los archivos deben residir localmente en la carpeta del sistema.
* **Validaciones y posibles errores:** Archivos corruptos o bloqueados por el sistema operativo.

## 6. Generación de Reportes
* **Nombre del proceso:** Reportes y Estadísticas del Sistema.
* **Objetivo:** Procesar los datos acumulados para entregar una visión clara del estado comercial y financiero.
* **Descripción del funcionamiento:** Recorre los archivos de productos y ventas para calcular listados, alertas de stock mínimo, ingresos totales, producto más vendido y valor total del inventario.
* **Datos de entrada:** Contenido actual de `productos.json` y `ventas.json`.
* **Procesamiento realizado:** Filtrados por condición de stock crítico (`cantidad <= stock_minimo`), sumatorias de ingresos, diccionarios de conteo para productos más vendidos y multiplicación de precio por cantidad para el valor de inventario.
* **Datos de salida:** Reporte estructurado impreso en consola.
* **Reglas de negocio:** Los cálculos deben derivarse estrictamente de los datos almacenados, sin valores quemados en código.
* **Validaciones y posibles errores:** Ausencia de registros previos que devuelvan valores vacíos o divisiones por cero.
