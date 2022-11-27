from django.urls import path
from app import views
from PGPI import settings
from django.conf.urls.static import static 
from . import views as v

urlpatterns = [
    path('botas/<int:id_botas>',v.detalleProd),
    path('',v.inicio),
    path('base', v.base),
    path('cestaDeCompra/', v.cestaDeCompra, name = "cestaDeCompra"),
    path('carritoDeCompra/', views.carritoDeCompra, name='carritoDeCompra')
]

+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
