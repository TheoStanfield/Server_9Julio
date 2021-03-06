from django.urls import path
from . import views

app_name= 'usuario'
urlpatterns = [
    path('', views.tablaIngresos, name='entrada-respuesta'),#respuesta/
    path('cargar/',views.cargarDB, name='cargarDB'),
    path('tarjetas/',views.nrTarjeta, name='tarjeta'),
    path('tarjetas/<int:id>/',views.vincular, name='vincular')
]
