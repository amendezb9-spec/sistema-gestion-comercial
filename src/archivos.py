
import json
import os
import tempfile
from pathlib import Path



BASE = Path(__file__).resolve().parent.parent


DATA = BASE / "data"



def leer(nombre, defecto=None):
    ruta = DATA / nombre

    if not ruta.exists():
        return [] if defecto is None else defecto

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        if not isinstance(datos, list):
            raise ValueError("El archivo no contiene una lista.")

        return datos

    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(
            f"Error al leer el archivo {nombre}: {error}"
        ) from error



def guardar(nombre, datos):
    DATA.mkdir(parents=True, exist_ok=True)

    temporal = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=DATA,
            delete=False,
            suffix=".tmp"
        ) as archivo:

            temporal = Path(archivo.name)

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

            archivo.flush()
            os.fsync(archivo.fileno())

        os.replace(temporal, DATA / nombre)

    finally:
        if temporal is not None and temporal.exists():
            temporal.unlink()



if __name__ == "__main__":
    print("Modulo de archivos listo.")
