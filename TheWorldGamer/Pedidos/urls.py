from django.urls import path
from Pedidos import views

urlpatterns = [
    path('Pedidos/', views.pedidos, name="Pedidos"),
    path('Pedido_creado/', views.crearPedido, name="Pedido_creado"),
    path('Dar_voto/<str:Nombre>', views.dar_voto, name="Dar_voto"),
]



