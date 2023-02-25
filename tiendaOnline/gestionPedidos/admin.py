from django.contrib import admin
from gestionPedidos.models import Cliente, Articulo, Pedidos


# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'email', 'tel')
    search_fields = ('nombre', 'direccion', 'email', 'tel')


class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'seccion', 'precio')
    search_fields = ('nombre', 'seccion', 'precio')
    list_filter = ('nombre', 'seccion', 'precio')



class PedidoAdmin(admin.ModelAdmin):
    list_filter = ('numero', 'fecha', 'entregado')
    list_display = ('numero', 'fecha','entregado')
    search_fields = ('numero', 'fecha', 'entregado')
    date_hierarchy = 'fecha'


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Pedidos, PedidoAdmin)
