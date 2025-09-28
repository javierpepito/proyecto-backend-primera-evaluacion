from django.shortcuts import render, get_object_or_404, redirect
from .models import Visitante
from .forms import VisitanteForm

def lista_visitas(request):
    visitantes = Visitante.objects.all()
    return render(request, 'SistemaRegistros/lista_visitas.html', {'visitantes': visitantes})

def registrar_visita(request):
    if request.method == 'POST':
        form = VisitanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = VisitanteForm()
    return render(request, 'SistemaRegistros/registrar_visita.html', {'form': form})

""""
def editar_visitante(request, id):
    visitante = get_object_or_404(Visitante, id=id)
    if request.method == 'POST':
        form = VisitanteForm(request.POST, instance=visitante)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = VisitanteForm(instance=visitante)
    return render(request, 'SistemaRegistros/editar_visitante.html', {'form': form})


def eliminar_visitante(request, id):
    visitante = get_object_or_404(Visitante, id=id)
    if request.method == 'POST':
        visitante.delete()
        return redirect('lista_visitas')
    return render(request, 'SistemaRegistros/eliminar_visitante.html', {'visitante': visitante})"""