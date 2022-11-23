from django.shortcuts import render

# Create your views here.
def devolucion(request):
    return render(request, 'devoluciones.html')