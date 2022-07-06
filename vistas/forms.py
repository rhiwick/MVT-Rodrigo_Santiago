from mailbox import NoSuchMailboxError
from django import forms

class crear_producto(forms.Form):
    productoCia =  forms.CharField(max_length=30)
    productoCodigo = forms.CharField()
    productoDescripcion = forms.CharField()
    productoCantidad = forms.IntegerField()
    productoCosto = forms.IntegerField()
    
class busqueda_producto(forms.Form):
    productoCodigo = forms.CharField(max_length=30)
    