from django.contrib import admin
from .models import Visita
from django.utils import timezone
from django.contrib import messages
import pytz

def obtener_hora_chile():
    chile_tz = pytz.timezone('America/Santiago')
    return timezone.now().astimezone(chile_tz).time()

# Register your models here.
@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista
    list_display = ('rut', 'nombre', 'motivo_visita', 'fecha_visita', 'hora_entrada', 'hora_salida')
    
    # Búsqueda por RUT y nombre
    search_fields = ('rut', 'nombre')
    
    # Filtros por fecha en la barra lateral
    list_filter = ('fecha_visita',)
    
    # Se registran las acciones masivas
    actions = ['marcar_salida_ahora']

    # Organizar campos en el formulario de edición 
    fieldsets = (
        ('Información Personal', {
            'fields': ('rut', 'nombre')
        }),
        ('Información de la Visita', {
            'fields': ('motivo_visita', 'fecha_visita', 'hora_entrada', 'hora_salida')
        }),
    )
    
    # Ordenamiento por defecto
    ordering = ('-fecha_visita', '-hora_entrada')
    
    # Número de registros por página
    list_per_page = 15
    
    # Formato de fecha en la lista 
    date_hierarchy = 'fecha_visita'

    # Acción: Actualizar salida de visitas
    @admin.action(description='Actualizar hora de salida (hora actual)')
    def marcar_salida_ahora(self, request, queryset):
   
        # Obtener hora actual de Chile
        hora_actual = obtener_hora_chile()
        
        # Actualizar todas las visitas seleccionadas
        total_actualizado = queryset.update(hora_salida=hora_actual)
        
        # Mensaje simple y directo
        self.message_user(
            request,
            f"✓ Se actualizó la hora de salida de {total_actualizado} visita(s) a las {hora_actual.strftime('%H:%M:%S')}",
            messages.SUCCESS
        )

#admin.site.site_header = "Panel Interno — Registro de Visitas"
#admin.site.site_title = "Admin Registro de Visitas"
#admin.site.empty_value_display = '-Sin datos-'