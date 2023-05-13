from django.urls import path
from Usuarios.views import user_registro, cerrar_sesion, iniciar_sesion

urlpatterns = [
    
    path('Registrarse/', user_registro.as_view(), name="autenticacion"),
    path('Cerrar_sesion/', cerrar_sesion, name="Cerrar_sesion"),
    path('Iniciar_sesion/', iniciar_sesion, name="Iniciar_sesion")
  
]



