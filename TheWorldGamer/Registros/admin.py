from django.contrib import admin

from Registros.models import Registro

# Register your models here.

class Busqueda_registro(admin.ModelAdmin):

    list_filter=("Seccion",)
    list_display=("Usuario", "Id_usuario", "Juego", "Seccion", "Precio", "Tiempo", "Created", "alquiladas") 
    search_fields=("Nombre", "Usuario") 
    readonly_fields=("Created",)
    date_hierarchy="Created" 

admin.site.register(Registro, Busqueda_registro)