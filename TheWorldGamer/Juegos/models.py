from django.db import models

# Create your models here.
    
class Seccion_Juego(models.Model):

    Seccion = models.CharField(max_length=50)
    
    class Meta:
        
        verbose_name = "Seccion"
        verbose_name_plural = "Secciones"
        
    def __str__(self):
        
        return self.Seccion
    
class Juego(models.Model):

    Nombre = models.CharField(max_length=50)
    Seccion = models.ForeignKey(Seccion_Juego, on_delete=models.CASCADE)
    Imagen = models.ImageField(upload_to="juegos", null=True,  blank=True)
    Precio = models.IntegerField()
    
    class Meta:
        
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"
        
    def __str__(self):
        
        return self.Nombre

