from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.conf import settings

from app.models import Botas, BotasCarrito
from .forms import BotasCarritoForm
from django.template import RequestContext
from app.models import Botas



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

def buscar_bota(request):
    
    if request.method == "POST":
        searched = request.POST['searched']
        return render(request, 'buscar.html',{'searched':searched})
    else:
       return render(request, 'buscar.html',{'searched':searched})

    
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

