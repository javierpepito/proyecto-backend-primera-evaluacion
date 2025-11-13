## Caso Escogido: Sistema de Registro de Visitas para una Empresa
**Contexto**  Una empresa necesita llevar un control digital de las visitas que recibe diariamente.

**Requerimientos**
* Registrar nombre, RUT, motivo de visita y hora de entrada/salida.
* Mostrar listado de visitas del día.
* Utilizar estructuras de decisión para validar datos.

### Modelo de Visitante
- nombre
- rut
- motivo_visita
- fecha_visita
- hora_entrada
- hora_salida

### Preguntar si la pagina va dirigida a que los visitantes se anoten o un admin
> El foco depende de ustedes, pero deben de solucionar la problematica cumpliendo con la escala de apreciación adjunta en el PDF.

## Escala de apreciacion
1. Identifica correctamente variables y operaciones del lenguaje: Que sepan identificar las variables y nombres pertenecientes a los modulos de Django.
2. Utiliza estructuras de decisión y operadores de forma adecuada: Validan información y la lógica de código es correcta.
3. Integra paquetes externos en la solución: Que sepan cómo instalar y utilizar Django como paquete de Python-
4. Implementa una aplicación funcional en Django según requerimientos: Soluciona el problema ocupando el Framework de Django.
5. Estructura el código de forma clara y ordenada: El codigo no presenta problemas de identación.
6. Comenta el código para facilitar su comprensión: Comenta el código con comentarios de linea o acompañados de archivos tipo .md (Markdown)
7. Valida correctamente los datos de entrada: Válida y asegura que la información ingresada sea correcta o apta para su uso informático.
8. Utiliza correctamente el entorno de desarrollo y herramientas asociadas: Presenta el proyecto con VENV y respeta estructura del proyecto.
9. Cumple con los requerimientos funcionales del caso seleccionado: Soluciona todos los enunciados del caso seleccionado.
10. Presenta el archivo sin errores de ejecución: Sin errores.

## Convención de commits:
- `feat`: caracteristica nueva
- `fix`: arreglo de un error
- `style`: estilizar las interfaces sin agregar grandes caracteristicas nuevas
- `refactor`: se cambia como funciona un modulo

# Comandos para utilizar en el proyecto
```bash
python -m venv venv
```

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

```bash
python manage.py runserver
```
```bash
python manage.py collectstatic
```

## COLORES
* Navbar: #262b40
* Fondo claro: #B8D9FF
* Fondo oscuro: #004CA3
* Footer: #013c80
* Bordes: grey

## Trabajo Pendiente
* Responsividad especialmente con la imagen, ademas agregar Font Tecnologico.

## Despliege Heroku

``` bash
python -m pip install -r requirements.txt
```


### comando para estar en python mas actualizado

```bash
c:\ProgramData\anaconda3\Scripts\activate.bat
```

```bash
venv\Scripts\activate
```

```bash
python manage.py createsuperuser
```

### Dudas y cosas a realizar
* Admin: filtros por fecha, búsqueda por RUT, acciones masivas (marcar salida)
* ejecuccion de migraciones
* conexion de supabase a render
* archivos estaticos
* paginacion de listados

@admin.register(NombreClase)
class NombreClaseAdmin(admin:ModelAdmin):
    date_hierarchy -->
    list_display -->
    search_fields -->
    list_filter -->

    @admin.display(description="Total")
    def total_display(self, obj):
        return f"${obj.total:,.0f}"

### Mejorar en Markdown
> Ver videos tutoriales de todos los posibles diseños.