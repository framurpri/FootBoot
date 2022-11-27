from django.shortcuts import render, get_object_or_404, HttpResponse
from django.conf import settings
from app.models import Botas



# Create your views here.

def detalleProd(request,id_botas):
   
    
    
    dato = get_object_or_404(Botas, pk=id_botas)
    
    return render(request,'detalleProd.html',{'botas':dato})


def base(request):
   
    
    
    dato = get_object_or_404(Botas)
    
    return render(request,'detalleProd.html',{'botas':dato})


def carritoDeCompra(request):

    botas = Botas.objects.all()

    return render(request, 'carritoDeCompra.html', {'botas':botas})

def inicio(request):

    botas= Botas.objects.all()

    return render(request,'inicio.html',{'botas':botas})