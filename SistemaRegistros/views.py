from django.shortcuts import render, get_object_or_404, redirect
from .models import Visita
from .forms import VisitaForm
from datetime import date
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import GroupSerializer, UserSerializer, VisitaSerializer
from django.http import JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all().order_by("nombre")
    serializer_class = VisitaSerializer
    permission_classes = [permissions.IsAuthenticated]

def custonm_endpoint(request):
    return JsonResponse({
        "secretos": "dasdasfasds"
    })

#Vista para ver visitas diarias
def lista_visitas(request):
    hoy = date.today()  
    visitas = Visita.objects.filter(fecha_visita=hoy)
    return render(request, 'SistemaRegistros/lista_visitas.html', {'visitas': visitas, 'fecha_actual':hoy})

#Vista para ver todas las visitas
def lista_completa(request): 
    visitas = Visita.objects.all() 
    return render(request, 'SistemaRegistros/lista_completa.html', {'visitas': visitas})

#Vista para registrar visitas nuevas
def registrar_visita(request):
    mensaje_exito = ""
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje_exito = "Se ha registrado la visita con éxito."
            form = VisitaForm()
    else:
        form = VisitaForm()
    return render(request, 'SistemaRegistros/registrar_visita.html', {'form': form, 'mensaje_exito': mensaje_exito})

#Vista para editar visitas
def editar_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    if request.method == 'POST':
        form = VisitaForm(request.POST, instance=visita)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = VisitaForm(instance=visita)
    return render(request, 'SistemaRegistros/editar_visita.html', {'form': form})

#Vista para eliminar visitas
def eliminar_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    if request.method == 'POST':
        visita.delete()
        return redirect('lista_visitas')
    return render(request, 'SistemaRegistros/eliminar_visita.html', {'visita': visita})