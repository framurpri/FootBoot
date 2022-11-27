from django.contrib import admin

from app.models import Botas, Carrito, BotasCarrito

# Register your models here.

admin.site.register(Botas)
admin.site.register(Carrito)
admin.site.register(BotasCarrito)