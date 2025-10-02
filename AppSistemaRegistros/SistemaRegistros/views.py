from django.shortcuts import render, get_object_or_404, redirect
from .models import Visita
from .forms import VisitaForm
from .utils import validar_rut

def lista_visitas(request):
    visitas = Visita.objects.all()
    return render(request, 'SistemaRegistros/lista_visitas.html', {'visitas': visitas})

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

def editar_visita(request, rut):
    visita = get_object_or_404(Visita, rut=rut)
    if request.method == 'POST':
        form = VisitaForm(request.POST, instance=visita)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = VisitaForm(instance=visita)
    return render(request, 'SistemaRegistros/editar_visita.html', {'form': form})

def eliminar_visita(request, rut):
    visita = get_object_or_404(Visita, rut=rut)
    if request.method == 'POST':
        visita.delete()
        return redirect('lista_visitas')
    return render(request, 'SistemaRegistros/eliminar_visita.html', {'visita': visita})