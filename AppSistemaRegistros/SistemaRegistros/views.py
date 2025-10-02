from django.shortcuts import render, get_object_or_404, redirect
from .models import Visita
from .forms import VisitaForm
from datetime import date

def lista_visitas(request):
    hoy = date.today()  
    visitas = Visita.objects.filter(fecha_visita=hoy)
    return render(request, 'SistemaRegistros/lista_visitas.html', {'visitas': visitas, 'fecha_actual':hoy})

def lista_completa(request): 
    visitas = Visita.objects.all() 
    return render(request, 'SistemaRegistros/lista_completa.html', {'visitas': visitas})

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

def eliminar_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    if request.method == 'POST':
        visita.delete()
        return redirect('lista_visitas')
    return render(request, 'SistemaRegistros/eliminar_visita.html', {'visita': visita})