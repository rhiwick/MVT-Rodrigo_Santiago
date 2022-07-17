from mailbox import NoSuchMailboxError
from django import forms

class FormCrearProducto(forms.Form): #estos nombres tienen que ser por ejemplo: FormCrearProducto
    producto_cia =  forms.CharField(max_length=30)
    producto_codigo = forms.CharField()
    producto_descripcion = forms.CharField()
    producto_costo = forms.IntegerField(required=False)
    producto_fecha = forms.DateField(required=False)#aca pondria required=False
    
class FormBusquedaProducto(forms.Form):
    producto_codigo = forms.CharField(max_length=30)
    