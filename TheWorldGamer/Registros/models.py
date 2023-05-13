from django.db import models

# Create your models here.

class Registro(models.Model):
    
    Usuario = models.CharField(max_length=50)
    Id_usuario = models.CharField(max_length=50)
    Juego = models.CharField(max_length=50)
    Seccion = models.CharField(max_length=50)
    Img = models.ImageField()
    Precio = models.IntegerField()
    alquiladas = models.IntegerField()
    Tiempo = models.CharField(max_length=50)
    actualizacion = models.DateTimeField(auto_now=True)
    Created = models.DateTimeField(auto_now_add=True)
    
    class meta:
        
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        
    def __str__(self):
        
        return self.Juego