from django import forms
from .models import Visita
from django.core.exceptions import ValidationError
import re

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = '__all__'

    # --- Validación del RUT (solo formato, no unicidad) ---
    def clean_rut(self):
        rut = self.cleaned_data.get("rut", "").strip().upper()

        # Verificar formato: ########-X
        if not re.match(r'^\d{7,8}-[\dK]$', rut):
            raise ValidationError("El RUT debe tener el formato XXXXXXXX-X, con último dígito numérico o K.")

        return rut

    # --- Validación del nombre ---
    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre", "").strip()

        # Solo letras y espacios
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            raise ValidationError("El nombre solo puede contener letras y espacios.")

        if len(nombre) > 50:
            raise ValidationError("El nombre no puede superar los 50 caracteres.")

        return nombre

    # --- Validación del motivo ---
    def clean_motivo_visita(self):
        motivo = self.cleaned_data.get("motivo_visita", "").strip()

        if len(motivo) > 200:
            raise ValidationError("El motivo de la visita no puede superar los 200 caracteres.")

        return motivo

    # --- Validación de fechas/horas ---
    def clean(self):
        cleaned_data = super().clean()
        rut = cleaned_data.get("rut")
        fecha_visita = cleaned_data.get("fecha_visita")
        hora_entrada = cleaned_data.get("hora_entrada")
        hora_salida = cleaned_data.get("hora_salida")

        # Evitar visitas duplicadas en la misma fecha
        if rut and fecha_visita:
            existe = Visita.objects.filter(rut=rut, fecha_visita=fecha_visita).exists()
            if existe:
                raise ValidationError("Este visitante ya tiene una visita registrada en esta fecha.")

        # Validar que la hora de salida no sea antes que la de entrada
        if hora_entrada and hora_salida:
            if hora_salida < hora_entrada:
                raise ValidationError("La hora de salida no puede ser anterior a la hora de entrada.")

        return cleaned_data