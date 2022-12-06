import random
import string
from django.db import models
from django import forms

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
    imagen = models.ImageField(upload_to='', null=True, blank=True)
    agotado = models.BooleanField(default=False)

class Carrito(models.Model):
    creation_date = models.DateTimeField()

class BotasCarrito(models.Model):
    bota = models.ForeignKey(Botas, on_delete=models.CASCADE)
    #carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, null = True)
    cantidad = models.IntegerField()

    
def random_id(lenght=5):
    return ''.join(random.choice(string.digits) for x in range(lenght))    

class Pedido(models.Model):
    nombre=models.CharField(max_length=20, blank=False, null=False,help_text="Nombre")
    apellidos=models.CharField(max_length=20,blank=False, null=False)
    telefono = models.CharField(max_length=11,blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    direccion = models.CharField(max_length=150,blank=False, null=False)
    PAGO = (('Contrareembolso','Contrareembolso'),('PaaS','Paas'))
    formaPago = models.CharField(max_length=20,choices=PAGO,default="Contrareembolso",blank=False, null=False)
    idSeguimiento = models.CharField(max_length=5, default=random_id, editable=True)
    ESTADOS = (('En almacén','En almacén'), ('En reparto', 'En reparto'), ('Entregado', 'Entregado'))
    estado =  models.CharField(max_length=20,choices=ESTADOS,default="En almacén",blank=False, null=False)
    


class AtencionCliente(models.Model):
    email = models.EmailField(blank=False, null=False)
    asunto = models.CharField(max_length=150, null = False)
    descripcion = models.TextField(null=False)

class AtencionC(models.Model):
    email = models.EmailField(blank=False, null=False)
    asunto = models.CharField(max_length=150, null = False)
    descripcion = models.TextField(null=False)



    
    


