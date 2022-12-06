from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.conf import settings
from django.views import View
from app import models

from app.models import Botas, BotasCarrito, Pedido
from .forms import RegistroForm
from django.template import RequestContext
from app.models import Botas
from django.views.decorators.http import require_http_methods

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.


def base(request):

    return render(request,'base.html')

def carrito_de_compra(request):

    precio_total = calcula_precio_total()
    botas = BotasCarrito.objects.all()

    return render(request, 'carritoDeCompra.html', {'botasC':botas,'precioT':precio_total})

def calcula_precio_total():
    botas = BotasCarrito.objects.all()
    precio_total= 0.0
    for b in botas:
        
        precio_total+= float(b.cantidad)*float(b.bota.precio)
    return precio_total


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

class añadir_bota_al_carrito(View):
    
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
        precio = calcula_precio_total()

        return render(request, 'compra.html',{'precioT':precio})
    
    def post(self, request):
        if request.method == 'POST':
            email = request.POST.get('email')
            nombre = request.POST.get('nombre')
            apellidos = request.POST.get('apellidos')
            telefono = request.POST.get('telefono')
            direccion = request.POST.get('direccion')
            metodo_pago =request.POST.get('pago')
            precio = calcula_precio_total()
            print(email)
            print(metodo_pago)
            
            Pedido.objects.create(nombre=nombre,apellidos=apellidos,telefono=telefono,email=email,direccion=direccion,formaPago=metodo_pago)

            template = get_template('compra_realizada.html')

            # Se renderiza el template y se envias parametros
            content = template.render({'email': email,'nombre':nombre,'direccion':direccion,
            'apellidos':apellidos,'telefono':telefono,'metodoPago':metodo_pago,'precioT':precio})

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

def registro(request):
    data = {
        'form': RegistroForm()
    }

    if request.method == 'POST':
        formulario = RegistroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],email=formulario.cleaned_data["email"] , password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, 'Te has registrado correctamemete')
            return redirect(to="inicio")
        data['form'] = formulario
    return render(request, 'form_registro.html', data)

        

