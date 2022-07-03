from django.db import models

# Create your models here.


class Familiar(models.Model):
    nombre_familiar = models.CharField(max_length=30)
    edad_familiar = models.IntegerField()
    documento_familiar = models.IntegerField()
    

class Stock(models.Model):
    producto_cia = models.CharField(max_length=15)
    producto_codigo = models.CharField(max_length=10)
    producto_descripcion = models.CharField(max_length=30)
    producto_cantidad = models.IntegerField(null=0) #siempre empiezo en 0
    
    
    