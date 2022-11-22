from django.db import models

# Create your models here.

class Botas(models.Model):
    nombre = models.CharField(max_length=50)
    suela = models.CharField(max_length=50)
    gama =models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5,decimal_places=2)
    talla = models.PositiveIntegerField()

