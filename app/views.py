from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.conf import settings

from app.models import Botas, BotasCarrito, Pedido
from .forms import BotasCarritoForm
from django.template import RequestContext
from app.models import Botas
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.views import View


# Create your views here.

def detalleProd(request,id_botas):
    
    dato = get_object_or_404(Botas, pk=id_botas)

    return render(request,'detalleProd.html',{'botas':dato})


def base(request):
   
    return render(request,'base.html')

def carritoDeCompra(request):

    botas = Botas.objects.all()
    return render(request, 'carritoDeCompra.html', {'botas':botas})


def catalogo(request):

    botas = Botas.objects.all()
    return render(request, 'catalogo.html', {'botas':botas})

def cestaDeCompra(request):
    return render(request, 'cestaDeCompra.html')
    
def compra(request):
    botas = Botas.objects.all()
    return render(request, 'compra.html',{'botas':botas})

def inicio(request):

    botas= Botas.objects.all()
    return render(request,'inicio.html',{'botas':botas})

def añadirBotaAlCarrito(request, id_botas):

    formulario = BotasCarritoForm(request.POST or None)

    if formulario.is_valid():
        formulario.save()
        return redirect('app/carritoDeCompra')

    return render(request, 'formCreacionCarrito.html', {'formulario': formulario})


class Comprar(View):
    def get(self, request):
        return render(request, 'compra.html')
    
    def post(self, request):
        if request.method == 'POST':
            email = request.POST.get('email')
            nombre = request.POST.get('nombre')
            apellidos = request.POST.get('apellidos')
            telefono = request.POST.get('telefono')
            direccion = request.POST.get('direccion')
            metodoPago =request.POST.get('pago')
            print(email)
            print(metodoPago)

            Pedido.objects.create(nombre=nombre,apellidos=apellidos,telefono=telefono,email=email,direccion=direccion,formaPago=metodoPago)

            template = get_template('compra_realizada.html')

            # Se renderiza el template y se envias parametros
            content = template.render({'email': email,'nombre':nombre,'direccion':direccion,
            'apellidos':apellidos,'telefono':telefono,'metodoPago':metodoPago})

            # Se crea el correo (titulo, mensaje, emisor, destinatario)
            msg = EmailMultiAlternatives(
                'Gracias por tu compra',
                'Hola, te enviamos un correo con tu factura',
                settings.EMAIL_HOST_USER,
                [email]
            )

            msg.attach_alternative(content, 'text/html')
            msg.send()

        return render(request, 'catalogo.html')