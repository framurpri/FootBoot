from django.shortcuts import render, get_object_or_404, HttpResponse
from django.conf import settings
from app.models import Botas



# Create your views here.

def detalleProd(request,id_botas):
    botas = Botas.objects.all()
    for b in botas:
        b.delete()
    Botas.objects.create(nombre='Mercurial',suela='FG',gama='Alta',marca='Nike',precio=70.0,talla=45)
    Botas.objects.create(nombre='Copa mundial',suela='FG',gama='Alta',marca='Adidas',precio=100.0,talla=48)

    
    
    
    dato = get_object_or_404(Botas, pk=id_botas)
    return render(request,'inicio.html',{'botas':dato})




def inicio(request):

    botas= Botas.objects.all()

    return render(request,'inicio.html',{'botas':botas})