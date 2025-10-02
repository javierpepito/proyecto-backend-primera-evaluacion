# -----------------------------
# Funciones para RUT

def normalizar_rut(rut: str) -> str:
    """Quita espacios, puntos y pasa a mayúscula"""
    return rut.replace(" ", "").replace(".", "").upper()

def calcular_dv(rut_numeros: str) -> str:
    """Calcula el dígito verificador usando módulo 11"""
    suma = 0
    multiplicador = 2
    for numero in reversed(rut_numeros):
        suma += int(numero) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    resto = 11 - (suma % 11)
    if resto == 11:
        return "0"
    elif resto == 10:
        return "K"
    else:
        return str(resto)

def validar_rut(rut: str) -> str | None:
    """
    Valida un RUT chileno:
    - Formato ########-X
    - DV correcto según módulo 11
    - Mayúscula K permitida
    - No cuenta espacios ni puntos
    """
    rut = normalizar_rut(rut)

    if len(rut) < 3:
        return "El RUT es demasiado corto."

    if "-" not in rut:
        return "El RUT debe contener un guion antes del dígito verificador."

    numeros, dv = rut.split("-")

    if not numeros.isdigit():
        return "Los primeros caracteres deben ser números."

    dv = dv.upper()
    if not (dv.isdigit() or dv == "K"):
        return "El dígito verificador debe ser un número o la letra K."

    # Validar dígito verificador real
    if calcular_dv(numeros) != dv:
        return "El RUT ingresado no es válido (dígito verificador incorrecto)."

    return None  # si todo está bien

# -----------------------------
# Función para mostrar RUT con puntos
# -----------------------------
def formatear_rut(rut: str) -> str:
    """Da formato al RUT chileno: 22025650-2 → 22.025.650-2"""
    if not rut:
        return ""
    rut = rut.replace(".", "").upper()
    if "-" not in rut:
        return rut
    cuerpo, dv = rut.split("-")
    cuerpo = cuerpo[::-1]
    partes = [cuerpo[i:i+3] for i in range(0, len(cuerpo), 3)]
    cuerpo = ".".join(partes)[::-1]
    return f"{cuerpo}-{dv}"