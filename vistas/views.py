
from django.http import HttpResponse
from datetime import datetime
from vistas.models import Familiar

from django.template import Template, Context, loader


def inicio(request):
    principal = loader.get_template('inicio.html')
    nombre = 'Santiago Navalon'
    nombre2 = "Rodrigo Gimenez"
    render1 = principal.render({'nombre': nombre, 'nombre2': nombre2})
    return HttpResponse(render1)


def mi_template(request):
    
    template1 = loader.get_template('inicio.html')

    nombre = 'Santiago Navalon'
    nombre2 = "Rodrigo Gimenez"
    #familiar = Familiar(nombre_familiar='Marcelo', edad_familiar=50)
    #familiar.save()
    render1 = template1.render(
        {'nombre': nombre, 'nombre2': nombre2})
    
    return HttpResponse(render1)


    
def crear_familiar(request, nombre_familiar, edad_familiar, documento_familiar):
    creacion = loader.get_template('crear.html')
    familiar = Familiar(nombre_familiar=nombre_familiar, edad_familiar=edad_familiar, documento_familiar=documento_familiar)
    familiar.save()
    diccionario = {'familiar':familiar}
    documento = creacion.render(diccionario)
    return HttpResponse(documento)
    
def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'fecha actual: {fecha_actual} ')



def vista_familiar(request):
    
    template = loader.get_template('listado_familia.html')
    lista_familiar = Familiar.objects.all()
    render = template.render({'lista_familiar': lista_familiar})
    return HttpResponse(render)