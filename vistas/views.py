
from email.policy import default
from datetime import datetime
from vistas.forms import FormCrearProducto, FormBusquedaProducto, FormEliminarProducto, FormEditarProducto


from django.shortcuts import redirect, render
from vistas.models import Producto

from django.template import Template, Context, loader


def inicio(request):
    return render(request, "index.html")


def index(request):
    return render(request, "index.html")


def crear_producto(request):
    if request.method == 'POST':
        form_crear_producto = FormCrearProducto(request.POST)
        if form_crear_producto.is_valid():
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


def busqueda_producto(request):
    id_producto = request.GET.get('producto_codigo')
    #productos_listado = Producto.objects.all()
    
    if id_producto:
        productos_listado = Producto.objects.filter(producto_codigo=id_producto)
        
    else:
        productos_listado = Producto.objects.all()
        form = FormBusquedaProducto()
    
    form = FormBusquedaProducto()
    return render(request, 'busqueda_producto.html', {'form':form,'productos_listado':productos_listado} )

def maestro_producto(request):
    return render(request, 'maestro.html')




        
def eliminar_producto(request):
    id_producto = request.GET.get('producto_codigo')
    productos_listado = Producto.objects.all()
    if id_producto:
        productos_listado = Producto.objects.filter(producto_codigo=id_producto)
    else:
        productos_listado = Producto.objects.all()
        form = FormEliminarProducto()
    form = FormEliminarProducto()
    return render(request, 'eliminar_producto.html', {'form':form,'productos_listado':productos_listado})

def elimine_producto(request, id):
    producto_a_eliminar = Producto.objects.get(id=id)
    producto_a_eliminar.delete()
    return redirect('eliminar_producto')



def editar_producto(request):
    id_producto = request.GET.get('producto_codigo')
    productos_listado = Producto.objects.all()
    if id_producto:
        productos_listado = Producto.objects.filter(producto_codigo=id_producto)
    else:
        productos_listado = Producto.objects.all()
        form = FormBusquedaProducto()
    form = FormBusquedaProducto()
    return render(request, 'editar_producto.html' ,{'form':form,'productos_listado':productos_listado})


def edite_producto(request, id):
    prod = Producto.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormEditarProducto(request.POST)
        if form.is_valid():
            prod.producto_codigo = form.cleaned_data.get('producto_codigo')
            prod.producto_descripcion = form.cleaned_data.get('producto_descripcion')
            prod.producto_costo = form.cleaned_data.get('producto_costo')
            prod.save()
            
            return redirect('editar_producto')
        
        else:
            
            return render(request, 'edite_producto.html', {'form': prod})

    form_edicion = FormEditarProducto(initial={'producto_cia': prod.producto_cia,'producto_codigo': prod.producto_codigo, 'producto_descripcion': prod.producto_descripcion, 'producto_costo': prod.producto_costo})
    print('entre')
    return render(request, 'edite_producto.html', {'form':form, 'prod':prod,})
