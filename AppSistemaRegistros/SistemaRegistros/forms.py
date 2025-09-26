from django import forms
from .models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = ["rut", "nombre", "motivo_vista", "fecha_visita", "hora_visita"]