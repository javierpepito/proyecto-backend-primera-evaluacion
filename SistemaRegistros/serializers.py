from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

class VisitaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visita
        fields = ["url", "rut", "nombre", "motivo_visita", "fecha_visita", "hora_entrada", "hora_salida"]