from django import template

register = template.Library()

@register.filter
def formatear_rut(rut: str) -> str:
    
    #Da formato al RUT chileno: 22025650-2 → 22.025.650-2
    
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