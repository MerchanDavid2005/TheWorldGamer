from django.urls import path
from .views import agregar_valor

urlpatterns = [
    path('alquilado/<int:id>', agregar_valor),
]
