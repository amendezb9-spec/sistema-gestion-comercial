---
```markdown
# Manual de Usuario - Sistema de Gestión Comercial

## 1. Presentación y Propósito del Sistema
Este programa permite administrar eficientemente las operaciones cotidianas de una pequeña empresa, facilitando el control de inventarios, el registro rápido de ventas con cálculo de impuestos y la obtención de reportes financieros al instante.

## 2. Requisitos para Usarlo
* Tener instalado **Python 3.8** o superior en la computadora.
* Contar con una terminal o consola de comandos.

## 3. Instrucciones para Iniciar y Cerrar el Programa
1. Abra la terminal y ubíquese en la carpeta del proyecto.
2. Escriba el comando de ejecución: `python src.main`
3. Para salir del sistema de forma segura, elija la **Opción 5** en el menú principal.

## 4. Explicación del Menú Principal
Al iniciar, verá un menú numerado del 1 al 5:
* **1. Módulo de Productos:** Administra el catálogo de productos.
* **2. Módulo de Ventas:** Realiza transacciones comerciales a clientes.
* **3. Módulo de Inventarios:** Registra entradas de producto y movimientos.
* **4. Módulo de Reportes y Estadísticas:** Muestra resumenes y alertas.
* **5. Salir del Sistema:** Cierra el sistema de forma seugra.

## 5. Procedimiento para Registrar, Consultar y Modificar Productos
* Ingrese a la opción **1**.
* Seleccione **1** para registrar (complete código, nombre, categoría, precio, cantidad inicial y stock mínimo).
* Seleccione **3** para ver el listado completo y verificar el estado actual de la mercancía.
* Seleccione **4** para modificar un producto escribiendo su código e introduciendo nuevos datos (o presionando Enter para conservar los valores anteriores).

## 6. Procedimiento para Registrar Ventas
* Ingrese a la opción **2**.
* Digite el código del producto que desea vender e indique la cantidad requerida. Repita este paso si el cliente lleva más artículos.
* Escriba `fin` para finalizar la lista de compra. El sistema calculará de forma automática el subtotal, el IVA (12%) y el total general a pagar, imprimiendo una factura en pantalla y actualizando el inventario.

## 7. Procedimiento para Consultar y Actualizar Inventario
* Ingrese a la opción **3**.
* Seleccione **1** para registrar entradas de inventario (por ejemplo, reposición de mercadería por proveedores), ingresando el código, la cantidad a sumar y una descripción.
* Seleccione **2** para ver el historial cronológico completo de movimientos.

## 8. Instrucciones para Generar y Consultar Reportes
* Ingrese a la opción **4**. El sistema generará instantáneamente:
  * El listado general de mercancía.
  * La alerta de productos con existencias iguales o inferiores al stock mínimo.
  * Los ingresos totales acumulados.
  * El producto con mayor cantidad de unidades vendidas.
  * El valor económico total del inventario disponible.

## 9. Mensajes de Error Más Frecuentes
* *"Opción inválida"*: Se ingresó una letra o un número no establecido en el sistema. Intente de nuevo.
* *"Error: La cantidad no puede ser un nuemero negativo"*: Se intentó registrar un valor menores a cero. Ingrese un precio válido.
* *"Stock insuficiente"*: Se intentó vender más unidades de las que físicamente hay en existencia.

## 10. Recomendaciones para Conservar los Archivos
* No elimine ni mueva los archivos `.json` ubicados dentro de la carpeta `src/`, ya que contienen la base de datos operativa de su negocio.
* Realice una copia de seguridad periódica de toda la carpeta `src/` para evitar perdida de información ante fallas del equipo.
