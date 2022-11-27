from django.db import models

# Create your models here.

class Botas(models.Model):
    nombre = models.CharField(max_length=50)
    suela = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    gama =models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5,decimal_places=2)
    talla = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='', null=True, blank=True)
    #imagen = models.CharField(max_length=255)


    def __str__(self):
        return self.nombre
