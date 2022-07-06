from django import forms

class crear_producto(forms.Form):
    productoCia =  forms.CharField()
    productoCodigo = forms.CharField()
    productoDescripcion = forms.CharField()
    productoCantidad = forms.IntegerField()
    productoCosto = forms.IntegerField()
    