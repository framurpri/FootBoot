from django.urls import path
from app import views
from PGPI import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('botas/<int:id_botas>',views.detalleProd), 
    path('base', views.base),
    path('',views.inicio),
    path('carritoDeCompra/', views.carritoDeCompra, name='carritoDeCompra')
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)