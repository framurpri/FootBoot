from django.urls import path
from . import views as v

urlpatterns = [
    path('botas/<int:id_botas>',v.detalleProd),
    path('',v.inicio),
    path('cestaDeCompra/', v.cestaDeCompra, name = "cestaDeCompra")
]