from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.conf import settings
from django.views import View
from app import models

from app.models import Botas, BotasCarrito, Pedido, AtencionCliente
from .forms import BotasCarritoForm
from django.template import RequestContext
from app.models import Botas
from django.views.decorators.http import require_http_methods

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.views import View
from app.models import AtencionCliente


# Create your views here.


def base(request):

    return render(request,'base.html')

def carritoDeCompra(request):

    precioTotal = calculaPrecioTotal()
    botasC = BotasCarrito.objects.all()

    return render(request, 'carritoDeCompra.html', {'botasC':botasC,'precioT':precioTotal})

def calculaPrecioTotal():
    botasC = BotasCarrito.objects.all()
    precioTotal= 0.0
    for b in botasC:
        
        precioTotal+= float(b.cantidad)*float(b.bota.precio)
    return precioTotal


def catalogo(request):

    botas = Botas.objects.all()
    return render(request, 'catalogo.html', {'botas':botas})

@require_http_methods(["POST"])
def buscar_bota(request):
    
    if request.method == "POST":
        searched = request.POST['searched']
        botas = Botas.objects.filter(nombre__contains=searched)
        return render(request, 'buscar.html',{'searched':searched, 'botas':botas})
    else:
       return render(request, 'buscar.html')

    

def compra(request):
    botas = Botas.objects.all()
    return render(request, 'compra.html',{'botas':botas})

def inicio(request):

    botas= Botas.objects.all()
    return render(request,'inicio.html',{'botas':botas})

class añadirBotaAlCarrito(View):
    
    def get(self,request,id_botas):
        
        dato = get_object_or_404(Botas, pk=id_botas)

        return render(request,'detalleProd.html',{'botas':dato})

        
    def post(self,request,id_botas):
        if request.method == 'POST':
            bota = get_object_or_404(Botas, pk=id_botas)
            cantidad =request.POST.get('cantidad')
            BotasCarrito.objects.update_or_create(bota=bota,cantidad = cantidad)    
            bota.talla = request.POST.get('talla')
            bota.gama = request.POST.get('gama')
            botas = Botas.objects.all()
        return render(request, 'catalogo.html', {'botas':botas})


class Comprar(View):
    def get(self, request):
        precioT = calculaPrecioTotal()

        return render(request, 'compra.html',{'precioT':precioT})
    
    def post(self, request):
        if request.method == 'POST':
            email = request.POST.get('email')
            nombre = request.POST.get('nombre')
            apellidos = request.POST.get('apellidos')
            telefono = request.POST.get('telefono')
            direccion = request.POST.get('direccion')
            metodoPago =request.POST.get('pago')
            precioT = calculaPrecioTotal()
            print(email)
            print(metodoPago)
            
            Pedido.objects.create(nombre=nombre,apellidos=apellidos,telefono=telefono,email=email,direccion=direccion,formaPago=metodoPago)

            template = get_template('compra_realizada.html')

            # Se renderiza el template y se envias parametros
            content = template.render({'email': email,'nombre':nombre,'direccion':direccion,
            'apellidos':apellidos,'telefono':telefono,'metodoPago':metodoPago,'precioT':precioT})

            # Se crea el correo (titulo, mensaje, emisor, destinatario)
            msg = EmailMultiAlternatives(
                'Gracias por tu compra',
                'Hola, te enviamos un correo con tu factura',
                settings.EMAIL_HOST_USER,
                [email]
            )

            msg.attach_alternative(content, 'text/html')
            msg.send()
        botas = Botas.objects.all()
        return render(request, 'catalogo.html', {'botas':botas})

       

class AtencionC(View):
    def get(self, request):
        return render(request, 'atencionCliente.html')
    
    def post(self, request):
        if request.method == 'POST':
            email = request.POST.get('email')
            asunto = request.POST.get('asunto')
            descripcion = request.POST.get('descripcion')
           
            models.AtencionC.objects.create(email=email, asunto = asunto, descripcion = descripcion)
            
           

            template = get_template('correo_atencionCliente.html')

            # Se renderiza el template y se envias parametros
            content = template.render({'email': email,'asunto':asunto,'descripcion':descripcion})

            # Se crea el correo (titulo, mensaje, emisor, destinatario)
            msg = EmailMultiAlternatives(
                'Gracias por contactar con nosotros.',
                'Hola, te enviamos un correo para informarte de que tu incidencia será resuelta lo antes posible.',
                settings.EMAIL_HOST_USER,
                [email]
            )

            msg.attach_alternative(content, 'text/html')
            msg.send()

        return render(request, 'inicio.html')

        

