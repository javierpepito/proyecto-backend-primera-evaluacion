#Funciones para el RUT y su facil uso dentro de forms.py

def formatear_rut(rut: str) -> str:
    #Se formatea para que quede estandarizado y sea facil de filtrar
    return rut.replace(" ", "").replace(".", "").upper()

def calcular_dv(rut_numeros: str) -> str:
    #Se usar modulo 11 para verificar que el RUT chileno sea real (En terminos matematicos, mas no existente)
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
    rut = formatear_rut(rut)
    
    #Validar longitud del RUT
    if len(rut) < 9:
        return "El RUT debe ser mayor o igual a 8 digitos, ademas del guion."

    #Validar existencia de un guion
    if "-" not in rut:
        return "El RUT debe contener un guion antes del dígito verificador."

    #Se separan los numeros antes del guion con el digito despues del guion
    numeros, dv = rut.split("-")

    #Que los caracteres antes del guion siempre sean numeros
    if not numeros.isdigit():
        return "Los primeros caracteres deben ser números."

    #Que el ultimo digito sea numero o la letra especifica "K"
    dv = dv.upper()
    if not (dv.isdigit() or dv == "K"):
        return "El dígito verificador debe ser un número o la letra K."

    # Validar dígito verificador 
    if calcular_dv(numeros) != dv:
        return "El RUT ingresado no es válido (dígito verificador incorrecto)."

    return None  