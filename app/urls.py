from django.urls import path
from app import views
from PGPI import settings
from django.conf.urls.static import static 
from . import views as v

urlpatterns = [
    path('botas/<int:id_botas>/',v.detalleProd),
    path('detalle/<int:id_botas>/',v.detalleProd, name="detalleProd"),
    path('base/', v.base),
    path('catalogo/', v.catalogo),
    path('añadirBotaAlCarrito/', v.añadirBotaAlCarrito),
    path('carritoDeCompra/', v.carritoDeCompra, name='carritoDeCompra'),
    path('compra/',v.Comprar.as_view(), name='compra'),
    path('',v.inicio, name ='inicio'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
