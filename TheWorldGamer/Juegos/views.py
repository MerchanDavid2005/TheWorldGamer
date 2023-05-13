from django.shortcuts import render

from .models import Juego
from Registros.models import Registro

# Create your views here.

def Juegos(request):
    
    juegos = Juego.objects.all()

    return render(request, "juegos/juegos.html", {"juegos" : juegos})

def busquedaJuego(request):

    buscado = request.POST["busqueda"]

    if (buscado == ""):

        resultado = Juego.objects.all()

    else:
        
        resultado = Juego.objects.filter(Nombre__icontains = buscado.capitalize())
        
        if len(resultado) > 0:
            
            mensaje = "Este es el resultado de tu busqueda"
        
        else:
            
            mensaje = "No se han encontrado resultados de tu busqueda"

    return render(request, "juegos/juegos.html", {"juegos" : resultado, "mensaje" : mensaje})

def categoriaJuego(request):
    
    categoria = request.POST["Categoria"]
    
    if (categoria == "Terror"): 
        
        resultado_por_categoria = Juego.objects.filter(Seccion = 1)
        categoria = "Terror"
        
    elif (categoria == "Shooter"):
        
        resultado_por_categoria = Juego.objects.filter(Seccion = 2)
        categoria = "Shooter"
        
    elif (categoria == "Accion"): 
        
        resultado_por_categoria = Juego.objects.filter(Seccion = 3)
        categoria = "Accion"
        
    elif (categoria == "Aventura"): 
        
        resultado_por_categoria = Juego.objects.filter(Seccion = 4)
        categoria = "Aventura"
        
    elif (categoria == "Rol"): 
        
        resultado_por_categoria = Juego.objects.filter(Seccion = 5)
        categoria = "Rol"
        
    elif (categoria == "Deportes"): 
        
        resultado_por_categoria = Juego.objects.filter(Seccion = 6)
        categoria = "Deportes"
        
    elif (categoria == "Plataformero"): 
        
        resultado_por_categoria = Juego.objects.filter(Seccion = 8)
        categoria = "Plataformero"
        
    else:
    
        resultado_por_categoria = Juego.objects.all()
        mensaje = "Juegos de todas las categorias"
        return render(request, "juegos/juegos.html", {"juegos" : resultado_por_categoria, "categoria" : mensaje})
        
    mensaje = "Juegos de categoria {}".format(categoria)
    
    return render(request, "juegos/juegos.html", {"juegos" : resultado_por_categoria, "categoria" : mensaje})


