from django.shortcuts import render

from Registros.models import Registro

# Create your views here.

def historial(request, id):

    historial = Registro.objects.filter(Id_usuario = id)

    if len(historial) > 0:

        mensaje = "Este es el historial de los juegos que has alquilado"

        return render(request, "perfil/historial.html", {"historial" : historial, "mensaje" : mensaje})
    
    else:

        mensaje = "Aun no has alquilado juegos"

        return render(request, "perfil/historial.html", {"historial" : historial, "mensaje" : mensaje})
    
#-----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------
    
def busqueda(request):

    nombre = request.POST["juego"]
    usuario = request.POST["id_usuario"]

    busqueda_nombre = Registro.objects.filter(Id_usuario = usuario, Juego__icontains = nombre)

    mensaje = "Este es el resultado de tu busqueda"

    return render(request, "perfil/historial.html", {"historial" : busqueda_nombre, "mensaje" : mensaje})

#-----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------

def categoria(request):

    categoria = request.POST["Categoria_historial"]
    usuario = request.POST["id_usuario"]
    
    if categoria == "Terror": 

        resultado_por_categoria = Registro.objects.filter(Id_usuario = usuario, Seccion = "Terror")
        categoria = "Terror"
        
    elif categoria == "Shooter":
        
        resultado_por_categoria = Registro.objects.filter(Id_usuario = usuario, Seccion = "Shooter")
        categoria = "Shooter"
        
    elif categoria == "Accion": 
        
        resultado_por_categoria = Registro.objects.filter(Id_usuario = usuario, Seccion = "Accion")
        categoria = "Accion"
        
    elif categoria == "Aventura": 
        
        resultado_por_categoria = Registro.objects.filter(Id_usuario = usuario, Seccion = "Aventura")
        categoria = "Aventura"
        
    elif categoria == "Rol": 
        
        resultado_por_categoria = Registro.objects.filter(Id_usuario = usuario, Seccion = "Rol")
        categoria = "Rol"
        
    elif categoria == "Deportes": 
        
        resultado_por_categoria = Registro.objects.filter(Id_usuario = usuario, Seccion = "Deportes")
        categoria = "Deportes"
        
    elif categoria == "Plataformero": 
        
        resultado_por_categoria = Registro.objects.filter(Id_usuario = usuario, Seccion = "Plataformero")
        categoria = "Plataformero"
        
    else:
    
        resultado_por_categoria = Registro.objects.filter(Id_usuario = usuario)
        mensaje = "Juegos de todas las categorias"
        return render(request, "perfil/historial.html", {"historial" : resultado_por_categoria, "mensaje" : mensaje})
    
    if len(resultado_por_categoria) > 0:
            
        mensaje = "Juegos de categoria {}".format(categoria)
        
        return render(request, "perfil/historial.html", {"historial" : resultado_por_categoria, "mensaje" : mensaje})
    
    else:
        
        mensaje = "Juegos de caterogia de {}".format(categoria)
        
        alerta = "No tienes juegos alquilados acordes a esta categoria"
        
        return render(request, "perfil/historial.html", {"historial" : resultado_por_categoria, "mensaje" : mensaje, "alerta" : alerta})

#-----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------

def limites(request):
    
    limite = request.POST["limite_historial"]
    usuario = request.POST["id_usuario"]
    
    if limite == "7 dias":
        
        resultado_por_plazo = Registro.objects.filter(Id_usuario = usuario, Tiempo = "7 dias")
        plazo = "7 dias"
        
    elif limite == "15 dias":
        
        resultado_por_plazo = Registro.objects.filter(Id_usuario = usuario, Tiempo = "15 dias")
        plazo = "15 dias"
        
    elif limite == "1 mes":
        
        resultado_por_plazo = Registro.objects.filter(Id_usuario = usuario, Tiempo = "1 mes")
        plazo = "1 mes"
        
    elif limite == "3 meses":
        
        resultado_por_plazo = Registro.objects.filter(Id_usuario = usuario, Tiempo = "3 meses")
        plazo = "3 meses"
        
    elif limite == "6 meses":
        
        resultado_por_plazo = Registro.objects.filter(Id_usuario = usuario, Tiempo = "6 meses")
        plazo = "6 meses"
        
    elif limite == "1 año":
        
        resultado_por_plazo = Registro.objects.filter(Id_usuario = usuario, Tiempo = "1 año")
        plazo = "1 año"
        
    else:
        
        resultado_por_plazo = Registro.objects.filter(Id_usuario = usuario)
        mensaje = "Juegos de todos las plazos" 
        return render(request, "perfil/historial.html", {"historial" : resultado_por_plazo, "mensaje" : mensaje})
    
    if len(resultado_por_plazo) > 0:
        
        mensaje = "Juegos de con plazo de {}".format(plazo)
        
        return render(request, "perfil/historial.html", {"historial" : resultado_por_plazo, "mensaje" : mensaje})
    
    else:
        
        mensaje = "Juegos de plazo de {}".format(plazo)
        
        alerta = "No tienes juegos alquilados acordes a este plazo"
        
        return render(request, "perfil/historial.html", {"historial" : resultado_por_plazo, "mensaje" : mensaje, "alerta" : alerta})

        
    
