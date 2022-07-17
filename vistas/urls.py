



from .views import inicio, index, crear_producto, busqueda_producto, maestro_producto, editar_producto
from django.urls import path

urlpatterns = [
    path('', inicio),
    path('index/', index, name= 'index'),
    path('crear-stock/', crear_producto, name = 'crear_producto'),
    path('maestro/', maestro_producto, name = 'maestro'),
    path('editar_producto/', editar_producto, name = 'editar_producto'),
    path('busqueda/' ,busqueda_producto, name = 'busqueda_producto')

    
]