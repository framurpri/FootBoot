from django.shortcuts import render

# Create your views here.
def devolucion(request):
    return render(request, 'devoluciones.html')

def envio(request):
    return render(request, 'envio.html')

def cliente(request):
    return render(request, 'cliente.html')

def privacidad(request):
    return render(request, 'privacidad.html')
def terminos(request):
    return render(request, 'terminos.html')
def empresa(request):
    return render(request, 'empresa.html')