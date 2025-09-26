from django.urls import path
from.import views

urlpatterns = [
    path("", views.lista_visitantes, name="lista_visitantes"),
    #path("visitante/nuevo/", views.nuevo_visitante, name="nuevo_visitante"),
    #path("visitante/editar/<int:id>/", views.editar_visitante, name="editar_visitante"),
    #path("visitante/eliminar/<int:id>/", views.eliminar_visitante, name="eliminar_visitante"),
]