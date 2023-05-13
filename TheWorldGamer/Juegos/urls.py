from django.urls import path
from Juegos import views

urlpatterns = [
    path('Juegos/', views.Juegos, name="Juegos"),
    path('Resultado/', views.busquedaJuego, name="Resultado_busqueda"),
    path('Categoria/', views.categoriaJuego, name="Categoria_Juego")
]

