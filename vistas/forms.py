from django import forms

class crear_producto(forms.Form):
    productoCia =  forms.CharField()
    productoCodigo = forms.IntegerField()
    productoDescripcion = forms.IntegerField()
    productoCantidad = forms.IntegerField()
    productoCosto = forms.IntegerField()
    