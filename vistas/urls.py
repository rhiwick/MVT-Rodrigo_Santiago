from .views import inicio, ver_fecha, mi_template, vista_familiar, crear_familiar, index, crearProducto
from django.urls import path

urlpatterns = [
    path('', inicio),
    path('fecha/', ver_fecha),
    path('mi-template/', mi_template),
    path('index/', index, name= 'index'),
    path('crear-stock/', crearProducto, name = 'crear_producto'),
    #path('saludo/<nombre>', saludo),
    path('crear/<nombre_familiar>/<edad_familiar>/<documento_familiar>/', crear_familiar),
    path('listado-familia/', vista_familiar)
]