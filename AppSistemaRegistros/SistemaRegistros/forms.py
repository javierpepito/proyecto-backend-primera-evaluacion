from django import forms
from .models import Visita
from django.core.exceptions import ValidationError
from .utils import validar_rut, formatear_rut
import re
from datetime import date, timedelta, datetime
 
class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = '__all__'
        error_messages = {
            'nombre': {'max_length': "El nombre no puede superar los 50 caracteres.",},
            'motivo_visita': {'max_length': "El motivo de la visita no puede superar los 200 caracteres.",}
            }

    # Validación de RUT
    def clean_rut(self):
        rut = formatear_rut(self.cleaned_data.get('rut', ''))
        error = validar_rut(rut)
        if error:
            raise forms.ValidationError(error)
        return rut

    # Validación de nombre
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            raise ValidationError("El nombre solo puede contener letras y espacios.")
        
        """if len(nombre) > 50:
            raise ValidationError("El nombre no puede superar los 50 caracteres.")
        """
        return nombre
        
    # Validación de motivo de visita
    """def clean_motivo_visita(self):
        motivo = self.cleaned_data.get('motivo_visita', '').strip()
        if len(motivo) > 200:
            raise ValidationError("El motivo de la visita no puede superar los 200 caracteres.")
        return motivo"""

    def clean_fecha_visita(self):
        fecha_visita = self.cleaned_data.get('fecha_visita')
        rut = self.cleaned_data.get('rut')

        # Validar que no se pueda crear una fecha pasada al dia actual
        if fecha_visita:
            if fecha_visita < date.today():
                raise ValidationError("No se pueden registrar visitas para fechas pasadas.")

        if rut and fecha_visita:
            qs = Visita.objects.filter(rut=rut, fecha_visita=fecha_visita)
            # Excluir el registro actual si se está editando
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise ValidationError("Este visitante ya tiene una visita registrada en esta fecha.")

        return fecha_visita

    """def clean_hora_salida(self):
        hora_salida = self.cleaned_data.get('hora_salida')
        hora_entrada = self.cleaned_data.get('hora_entrada')
        if hora_salida and hora_entrada:
            if hora_salida < hora_entrada:
                raise ValidationError("La hora de salida no puede ser anterior a la hora de entrada.")
        return hora_salida"""

    def clean_hora_salida(self):
        hora_salida = self.cleaned_data.get('hora_salida')
        hora_entrada = self.cleaned_data.get('hora_entrada')

        if hora_salida and hora_entrada:
            today = datetime.today().date()
            dt_entrada = datetime.combine(today, hora_entrada)
            dt_salida = datetime.combine(today, hora_salida)

            # Permitimos que la hora sea pasado la media noche interpretando que es otro dia.
            if dt_salida < dt_entrada:
                dt_salida += timedelta(days=1)

            duracion = dt_salida - dt_entrada

            # Que la visita no dure mas de 12 horas.
            if duracion.total_seconds() > 12 * 3600:
                raise ValidationError("La hora de salida no puede ser antes que la hora de entrada, ni tampoco durar más de 12 horas.")

        return hora_salida
