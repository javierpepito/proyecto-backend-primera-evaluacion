from django.urls import path, include
from.import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", views.lista_visitas, name="lista_visitas"),
    path("visita/lista_completa", views.lista_completa, name="lista_completa"),
    path("visita/registrar/", views.registrar_visita, name="registrar_visita"),
    path("visita/editar/<int:id>/", views.editar_visita, name="editar_visita"),
    path("visita/eliminar/<int:id>/", views.eliminar_visita, name="eliminar_visita"),
]