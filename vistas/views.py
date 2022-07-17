
from email.policy import default
from django.http import HttpResponse
from datetime import datetime
from django import forms
from vistas.forms import FormCrearProducto, FormBusquedaProducto


from django.shortcuts import render
from vistas.models import Producto

from django.template import Template, Context, loader


# def inicio(request):
#     principal = loader.get_template('inicio.html')
#     nombre = 'Santiago Navalon'
#     nombre2 = "Rodrigo Gimenez"
#     render1 = principal.render({'nombre': nombre, 'nombre2': nombre2})
#     return HttpResponse(render1)

def inicio(request):
    return render(request, "index.html")


def index(request):
    return render(request, "index.html")


def crear_producto(request):
    if request.method == 'POST':
        form_crear_producto = FormCrearProducto(request.POST) #este crear producto es del form y la variable se deberia llamar form_crear_producto
        if form_crear_producto.is_valid(): #
            informacion = form_crear_producto.cleaned_data
            
            producto = Producto(producto_cia = informacion['producto_cia'],
                             producto_codigo = informacion['producto_codigo'], 
                             producto_descripcion = informacion['producto_descripcion'],
                             producto_costo = informacion['producto_costo'],
                             producto_fecha = datetime.now(),
                             producto_cantidad = 0
                             )
                             
            producto.save()
            
            return render(request, 'crear_stock.html')
    else:
        form_crear_producto = FormCrearProducto()
    
    return render(request,'crear_stock.html',{'miProducto':form_crear_producto, } )


def busqueda_producto(request): #cambiar nombre por todo minuscula con guion bajo
    id_producto = request.GET.get('producto_codigo') #nombre de busqueda y las variables en rojo tienen que ser en snakeeye
    productos_listado = Producto.objects.all()
    
    if id_producto:
        productos_listado = Producto.objects.filter(producto_codigo=id_producto)
        
    else:
        productos_listado = Producto.objects.all()
        form = FormBusquedaProducto() #
    
    form = FormBusquedaProducto() #form vacio
    return render(request, 'busqueda_producto.html', {'form':form,'productos_listado':productos_listado} )

def maestro_producto(request):
    return render(request, 'maestro.html')

def editar_producto(request):
    return render(request, 'editar_producto.html')