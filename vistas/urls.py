from .views import inicio, ver_fecha, mi_template, vista_familiar, crear_familiar, index, crear_producto
from django.urls import path

urlpatterns = [
    path('', inicio),
    path('fecha/', ver_fecha),
    path('mi-template/', mi_template),
    path('index/', index),
    path('crear-stock/', crear_producto),
    #path('saludo/<nombre>', saludo),
    path('crear/<nombre_familiar>/<edad_familiar>/<documento_familiar>/', crear_familiar),
    path('listado-familia/', vista_familiar)
]