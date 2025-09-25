from django.db import models

# Create your models here.
class Visitante(models.Model):
    nombre = models.CharField(max_length=100)