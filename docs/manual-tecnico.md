# Manual Técnico - Sistema de Gestión Comercial

## 1. Arquitectura del Software
El sistema está desarrollado bajo un modelo modular en **Python (versión 3.8+)**, desacoplando la lógica de negocio, la persistencia de datos y la interfaz de usuario por medio de paquetes internos.

## 2. Descripción de Módulos
* **`src/main.py`**: Punto de entrada principal. Controla el flujo del menú general del sistema mediante bucles `while` y validaciones de opciones numéricas.
* **`src/archivos.py`**: Módulo centralizado de persistencia. Utiliza la librería nativa `json` para leer y escribir archivos de texto estructurado garantizando codificación `utf-8`.
* **`src/productos.py`**: Gestiona el CRUD completo de artículos comerciales (altas, consultas, listados, modificaciones y desactivaciones lógicas).
* **`src/ventas.py`**: Administra el proceso de transacciones de caja, control de existencias en tiempo real, cálculo de subtotales, impuesto del IVA (12%) y generación de números de venta consecutivos.
* **`src/inventario.py`**: Controla las entradas de almacén y genera un registro histórico detallado de movimientos de inventario con marca temporal (`datetime`).
* **`src/reportes.py`**: Realiza agregaciones y cálculos estadísticos sobre los archivos de datos (existencias críticas, ingresos totales, producto líder en ventas, valorización del inventario).

## 3. Estructura de Almacenamiento (JSON)
* `productos.json`: Almacena diccionarios con claves: `codigo`, `nombre`, `categoria`, `precio`, `cantidad`, `stock_minimo`, `activo`.
* `ventas.json`: Almacena transacciones estructuradas con número de venta, fecha, arreglo de detalles, subtotal, iva y total.
* `inventario.json`: Almacena el historial con fecha, código, tipo de movimiento (`ENTRADA` / `VENTA`), cantidad y descripción.

## 4. Requisitos y Ejecución
No requiere librerías externas de terceros (`pip install` no es necesario). Ejecutar desde la raíz del proyecto con:
```bash
python -m src.main
