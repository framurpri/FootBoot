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
    imagen = models.CharField(max_length=500)


class Carrito(models.Model):
    creation_date = models.DateTimeField()

class BotasCarrito(models.Model):
    bota = models.ForeignKey(Botas, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, null = True)
    cantidad = models.IntegerField()