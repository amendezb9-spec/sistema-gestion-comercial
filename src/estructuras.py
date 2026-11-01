
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def texto_obligatorio(valor, campo):
    texto = str(valor).strip()
    if not texto:
        raise ValueError(f"{campo} es obligatorio.")
    return texto


def entero_no_negativo(valor, campo="Cantidad"):
    if isinstance(valor, bool) or not str(valor).strip().isdigit():
        raise ValueError(
            f"{campo} debe ser un entero no negativo."
        )
    return int(valor)


def precio_valido(valor):
    try:
        numero = Decimal(str(valor))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise ValueError(
            "El precio debe ser numérico."
        ) from exc

    if not numero.is_finite() or numero < 0:
        raise ValueError(
            "El precio no puede ser negativo."
        )

    if numero != numero.quantize(Decimal("0.01")):
        raise ValueError(
            "El precio admite como máximo dos decimales."
        )

    return str(numero.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    ))
