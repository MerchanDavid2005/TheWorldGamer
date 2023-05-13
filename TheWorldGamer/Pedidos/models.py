from django.db import models

# Create your models here.

class Pedido(models.Model):

    Usuario_pedido = models.CharField(max_length=50)
    Usuario_id = models.CharField(max_length=50)
    Nombre_pedido = models.CharField(max_length=100)
    Imagen_pedido = models.ImageField(upload_to="pedidos", null=True,  blank=True)
    Numero_pedido = models.IntegerField()
    Creacion_pedido = models.DateTimeField(auto_now_add=True)
    Actualizacion_pedido = models.DateTimeField(auto_now=True)

    class Meta:
        
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        
    def __str__(self):
        
        return self.Nombre_pedido
    
class votos(models.Model):
    
    Usuario_Nombre = models.CharField(max_length=50)
    Usuario_id = models.CharField(max_length=50)
    Votos = models.IntegerField()
    Created = models.DateTimeField(auto_now_add=True)
    Ultimo_voto = models.DateTimeField(auto_now=True)
    
    class Meta:
        
        verbose_name = "Voto"
        verbose_name_plural = "Votos"
        
    def __str__(self):
        
        return self.Usuario_Nombre

