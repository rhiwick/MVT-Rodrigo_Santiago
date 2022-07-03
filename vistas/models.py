from django.db import models

# Create your models here.


class Familiar(models.Model):
    nombre_familiar = models.CharField(max_length=30)
    edad_familiar = models.IntegerField()
    documento_familiar = models.IntegerField()
    

