from django.urls import path
from.import views

urlpatterns = [
    path("", views.lista_visitas, name="lista_visitas"),
    path("visita/registrar/", views.registrar_visita, name="registrar_visita"),
    #path("visita/editar/<int:id>/", views.editar_visitante, name="editar_visita"),
    #path("visita/eliminar/<int:id>/", views.eliminar_visitante, name="eliminar_visita"),
]