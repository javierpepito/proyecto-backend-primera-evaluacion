from django.db import models

# Create your models here.

#Modelo del visitante con campo fecha y hora por separado para facilitar su filtrado.
class Visitante(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    motivo_visita = models.TextField(max_length=500)
    fecha_visita = models.DateField()
    hora_visita = models.TimeField()

    def __str__(self):
        return self.nombre
    