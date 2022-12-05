from django.urls import path
from app import views
from PGPI import settings
from django.conf.urls.static import static 
from . import views as v

urlpatterns = [ 
    path('detalle/<int:id_botas>/',v.añadirBotaAlCarrito.as_view(), name="detalleProd"),
    path('base/', v.base),
    path('catalogo/', v.catalogo),
    path('añadirBotaAlCarrito/', v.añadirBotaAlCarrito.as_view()),
    path('carritoDeCompra/', v.carritoDeCompra, name='carritoDeCompra'),
    path('compra/',v.Comprar.as_view(), name='compra'),
    path('atencionCliente/',v.AtencionC.as_view(), name='atencionCliente'),
    path('',v.inicio, name ='inicio'),
    path('buscar/',v.buscar_bota,name="buscar_bota")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
