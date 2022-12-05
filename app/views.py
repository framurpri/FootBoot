from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.conf import settings
from django.views import View

from app.models import Botas, BotasCarrito
from .forms import BotasCarritoForm
from django.template import RequestContext
from app.models import Botas



# Create your views here.


def base(request):

    return render(request,'base.html')

def carritoDeCompra(request):

    botasC = BotasCarrito.objects.all()
    precioTotal= 0.0
    for b in botasC:
        
        precioTotal+= float(b.cantidad)*float(b.bota.precio)
    print(precioTotal)
    return render(request, 'carritoDeCompra.html', {'botasC':botasC,'precioT':precioTotal})

def catalogo(request):

    botas = Botas.objects.all()
    return render(request, 'catalogo.html', {'botas':botas})


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
            botasC = BotasCarrito.objects.all()


        return render(request, 'carritoDeCompra.html', {'botasC':botasC})

