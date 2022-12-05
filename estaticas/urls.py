from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from PGPI import settings
from . import views as v

    
    
    
    
urlpatterns = [
      
    path('devoluciones/', v.devolucion),
    path('envios/', v.envio),
    path('atencioncliente/', v.cliente),
    path('privacidad/', v.privacidad),
    path('terminos/', v.terminos),
    path('empresa/', v.empresa)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)