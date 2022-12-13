from django.urls import path
from PGPI import settings
from django.conf.urls.static import static 
from . import views as v

urlpatterns = [ 
    path('detalle/<int:id_botas>/',v.añadir_bota_al_carrito.as_view(), name="detalleProd"),
    path('base/', v.base),
    path('catalogo/', v.catalogo),
    path('añadirBotaAlCarrito/', v.añadir_bota_al_carrito.as_view()),
    path('carritoDeCompra/', v.carrito_de_compra, name='carritoDeCompra'),
    path('compra/',v.Comprar.as_view(), name='compra'),
    path('atencionCliente/',v.AtencionC.as_view(), name='atencionCliente'),
    path('seguimiento/',v.Seguimiento.as_view(), name='seguimiento'),
    path(' ',v.inicio, name ='inicio'),
    path('buscar/',v.buscar_bota,name="buscar_bota"),
    path('borrarBotaCarrito/<int:id_botaC>/',v.borrarElemCarrito,name="borrarElemCarrito"),
    path('filtroMarca/',v.filtro_marca,name="filtro_marca")

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
