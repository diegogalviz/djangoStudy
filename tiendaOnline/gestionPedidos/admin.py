from django.contrib import admin
from gestionPedidos.models import Cliente, Articulo, Pedidos
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'email' ,'tel')

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'seccion','precio')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Articulo,ArticuloAdmin)
admin.site.register(Pedidos)
