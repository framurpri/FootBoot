from django.db import models

# Create your models here.

class Botas(models.Model):
    nombre = models.CharField(max_length=50)
        

    TIPOS_SUELA=(("Cesped Natural","Cesped Natural"),
    ("Cesped Artificial","Cesped Artificial"),
    ("Indoor","Indoor"))    
    suela = models.CharField(max_length=30, choices=TIPOS_SUELA, default="Cesped Natural")
    descripcion = models.TextField(max_length=200)
    GAMAS =(("A","Alta"),
    ("M","Media"),
    ("B","Baja"))
    gama =models.CharField(max_length=2,choices=GAMAS,default="M")
    marca = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5,decimal_places=2)

    TALLAS=(("T38","38"),
    ("T39","39"),
    ("T40","40"),
    ("T41","41"),
    ("T42","42"),
    ("T43","43"),
    ("T44","44"),
    ("T45","45"),
    ("T46","46"))
    talla = models.CharField(max_length=3,choices=TALLAS,default="T42")
    imagen = models.CharField(max_length=500)


