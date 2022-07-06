from django.db import models

# Create your models here.


class Familiar(models.Model):
    nombre_familiar = models.CharField(max_length=30)
    edad_familiar = models.IntegerField()
    documento_familiar = models.IntegerField()
    

class Stock(models.Model):
    productoCia = models.CharField(max_length=15)
    productoCodigo = models.CharField(max_length=10)
    productoDescripcion = models.CharField(max_length=30)
    productoCantidad = models.IntegerField(null=0) #siempre empiezo en 0
    productoCosto = models.IntegerField(null=0)
    
    
    