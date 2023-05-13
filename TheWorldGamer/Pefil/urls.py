from django.urls import path
from Pefil import views

urlpatterns = [
    path('Historial/<int:id>', views.historial, name="Historial"),
    path('Busqueda/', views.busqueda, name="Busqueda"),
    path('Categoria_historial/', views.categoria, name="Categoria"),
    path('Plazo/', views.limites, name="Limites")
]



