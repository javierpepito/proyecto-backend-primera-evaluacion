from django.shortcuts import render, get_object_or_404, redirect
from .models import Visita
from .forms import VisitaForm

def lista_visitas(request):
    visitas = Visita.objects.all()
    return render(request, 'SistemaRegistros/lista_visitas.html', {'visitas': visitas})

def registrar_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = VisitaForm()
    return render(request, 'SistemaRegistros/registrar_visita.html', {'form': form})


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

""""
def eliminar_visitante(request, id):
    visitante = get_object_or_404(Visitante, id=id)
    if request.method == 'POST':
        visitante.delete()
        return redirect('lista_visitas')
    return render(request, 'SistemaRegistros/eliminar_visitante.html', {'visitante': visitante})"""