from django.urls import path
from Home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.entrada, name="Presentacion"),
    path('Inicio/', views.inicio, name="Inicio"),
    path('QuienSoy/', views.yo, name="QuienSoy"),
    path('Contactame/', views.contacto, name="Contacto"),
    path('Correo_enviado/', views.enviar_correo, name="Correo_enviado"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


