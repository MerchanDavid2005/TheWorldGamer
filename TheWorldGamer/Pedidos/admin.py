from django.contrib import admin

from Pedidos.models import Pedido, votos

# Register your models here.

class Registro_pedido(admin.ModelAdmin):

    search_fields=("Usuario_pedido", "Nombre_pedido",) 
    readonly_fields=("Creacion_pedido", "Actualizacion_pedido")
    list_display=("Usuario_pedido", "Usuario_id", "Nombre_pedido", "Numero_pedido", "Actualizacion_pedido") 
    date_hierarchy="Actualizacion_pedido" 
    
class Registro_voto(admin.ModelAdmin):
    
    list_display=("Usuario_Nombre", "Usuario_id", "Votos", "Ultimo_voto")
    date_hierarchy="Ultimo_voto"
    readonly_fields=("Created", "Ultimo_voto")

admin.site.register(Pedido, Registro_pedido)
admin.site.register(votos, Registro_voto)