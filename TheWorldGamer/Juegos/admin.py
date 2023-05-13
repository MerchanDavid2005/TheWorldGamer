from django.contrib import admin

from Juegos.models import Seccion_Juego, Juego

# Register your models here.

class VideoJuegos(admin.ModelAdmin):

    list_filter=("Seccion",)
    list_display=("Nombre", "Precio") 
    search_fields=("Nombre",) 

admin.site.register(Seccion_Juego)
admin.site.register(Juego, VideoJuegos)