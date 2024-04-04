from django.contrib import admin
from .models import Usuario, Cliente,  Producto, Venta

admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Producto)
# Register your models here.
