from django.contrib import admin

from app.models import Botas, Carrito, BotasCarrito, Pedido

# Register your models here.

admin.site.register(Botas)
admin.site.register(Carrito)
admin.site.register(BotasCarrito)
admin.site.register(Pedido)