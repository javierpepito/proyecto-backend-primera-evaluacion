from django import forms
from .models import Visita

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ["rut", "nombre", "motivo_visita", "fecha_visita", "hora_entrada", "hora_salida"]