from django.shortcuts import render, get_object_or_404, redirect
from .models import Visitante
from .forms import VisitanteForm

#READ (LIST)
def visitante_list(request):
    visitantes = Visitante.objects.all()
    return render(request, 'SistemaRegistros/visitante_list.html', {'object_list': visitantes})

# READ (Detail)
def visitante_detail(request, pk):
    visitante = get_object_or_404(Visitante, pk=pk)
    return render(request, 'SistemaRegistros/visitante_detail.html',{'object': visitante})

# CREATE
def visitante_create(request):
    if request.method == 'POST':
        form = VisitanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitante_list')
    else:
        form = VisitanteForm()
        return render(request, 'SistemaRegistros/visitante_form.html', {'form':form})

# UPDATE
def visitante_update(request, pk):
    visitante = get_object_or_404(Visitante, pk=pk)
    if request.method == 'POST':
        form = VisitanteForm(request.POST, instance=visitante)
    if form.is_valid():
        form.save()
        return redirect('visitante_list')
    else:
        form = VisitanteForm(instance=visitante)
        return render(request, 'SistemaRegistros/visitante_form.html', {'form':form})

# DELETE
def visitante_delete(request, pk):
    visitante = get_object_or_404(Visitante, pk=pk)
    if request.method == 'POST':
        visitante.delete()
        return redirect('visitante_list')
    return render(request,'SistemaRegistros/visitante_confirm_delete.html', {'object': visitante})