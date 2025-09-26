from django.contrib import admin
from django.urls import path, include
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',views.inicio),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('inventario/', include('inventario.urls'))
]
