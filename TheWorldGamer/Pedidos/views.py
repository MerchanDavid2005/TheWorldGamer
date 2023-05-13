from django.shortcuts import render, redirect

from .models import Pedido, votos

from Juegos.models import Juego

from datetime import datetime
from datetime import timedelta
from django.utils import timezone

# Create your views here.

def pedidos(request):

    Mayor = 0
    Intemedio = 0
    Ultimo = 0
    nadie = 0
    
    centinela1 = 0
    centinela2 = 0
    centinela3 = 0

    Mas_pedidos = []

    Pedidos = Pedido.objects.all()

    for i in Pedidos:
        
        if i.Numero_pedido >= Mayor:
            
            if centinela3 > 0:
                
                nadie = Ultimo
                
                objeto4 = objeto3

            if centinela2 > 0:
                    
                Ultimo = Intemedio

                objeto3 = objeto2
            
            if centinela1 > 0:
            
                Intemedio = Mayor

                objeto2 = objeto1
            
            Mayor = i.Numero_pedido

            objeto1 = i.Nombre_pedido
            
            centinela1 +=1
            
        elif i.Numero_pedido <= Mayor and i.Numero_pedido >= Intemedio:
            
            if centinela3 > 0:
                
                nadie = Ultimo
                
                objeto4 = objeto3
            
            if centinela2 > 0:
            
                Ultimo = Intemedio

                objeto3 = objeto2
            
            Intemedio = i.Numero_pedido 

            objeto2 = i.Nombre_pedido
            
            centinela2 += 1

        elif i.Numero_pedido <= Intemedio and i.Numero_pedido >= Ultimo:
            
            if centinela3 > 0:
            
                nadie = Ultimo

                objeto4 = objeto3
            
            Ultimo = i.Numero_pedido 

            objeto3 = i.Nombre_pedido
            
            centinela3 += 1
    
    if Mayor != 0:
        
        Primero = Pedido.objects.get(Nombre_pedido = objeto1)
        Mas_pedidos.append(Primero)
        
    if Intemedio != 0:
        
        Segundo = Pedido.objects.get(Nombre_pedido = objeto2)
        Mas_pedidos.append(Segundo)
        
    if Ultimo != 0: 
        
        Tercero = Pedido.objects.get(Nombre_pedido = objeto3)
        Mas_pedidos.append(Tercero)

    mensaje = "Juegos mas pedidos"
    
    return render(request, "pedidos/pedidos.html", {"Pedidos" : Mas_pedidos, "Mensaje_juegos" : mensaje})

# --------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------

def crearPedido(request):

    Usuario_pedido = request.POST["usuario_nombre"]
    Usuario_id = request.POST["usuario_id"]
    Nombre_pedido = request.POST["Nombre_pedido"]
    Imagen_pedido = request.FILES["Imagen_pedido"]
        
    Juegos_en_funcion = Juego.objects.all()
    Juegos_pedidos = Pedido.objects.all()
    total_votos = votos.objects.all()

    hoy = timezone.now()

    for i in Juegos_en_funcion:
                
        if i.Nombre.lower() == Nombre_pedido.lower().strip():

            mensaje_pedido = "El juego pedido ya esta disponible en la pagina"
            return render(request, "pedidos/pedidos.html", {"Mensaje" : mensaje_pedido})     

    for v in total_votos:

        fecha_voto = v.Ultimo_voto.date()

        if v.Usuario_id == Usuario_id:

            for p in Juegos_pedidos:

                fecha_pedido = p.Actualizacion_pedido.date()

                if p.Nombre_pedido.lower() == Nombre_pedido.lower().strip():
                        
                    if fecha_voto != hoy.date():

                        v.Votos += 1
                        v.save()
                        p.Numero_pedido += 1
                        p.save()
                        mensaje_pedido = "El juego pedido ya ha sido pedido por otros usuarios, añadimos tu voto"
                        return render(request, "pedidos/pedidos.html", {"Mensaje" : mensaje_pedido})           
                        
                    else:
                        
                        mensaje_pedido = "El juego pedido ya ha sido pedido por otros usuarios, no puedes votar mas de 1 vez por dia" 
                        return render(request, "pedidos/pedidos.html", {"Mensaje" : mensaje_pedido})
                    
    for j_p in Juegos_pedidos:

        if j_p.Usuario_id == Usuario_id:

            fecha_pedido = j_p.Actualizacion_pedido.date()

            if fecha_pedido == hoy.date():
                        
                mensaje_pedido = "No puedes realizar mas de un pedido por dia" 
                return render(request, "pedidos/pedidos.html", {"Mensaje" : mensaje_pedido})
    
    for p in Juegos_pedidos:

        if p.Nombre_pedido.lower() == Nombre_pedido.lower().strip():
                        
            votos.objects.create(Usuario_Nombre = Usuario_pedido, Usuario_id = Usuario_id, Votos = 1)
            p.Numero_pedido += 1
            p.save()
            mensaje_pedido = "El juego pedido ya ha sido pedido por otros usuarios, añadimos tu voto"
            return render(request, "pedidos/pedidos.html", {"Mensaje" : mensaje_pedido}) 
    
    pedido_aceptado = Pedido.objects.create(Usuario_pedido = Usuario_pedido, Usuario_id = Usuario_id, Nombre_pedido = Nombre_pedido, Imagen_pedido = Imagen_pedido, Numero_pedido = 1)
    mensaje_pedido = "Tu pedido se ha realizado exitosamente" 
    return render(request, "pedidos/pedidos.html", {"Mensaje" : mensaje_pedido}) 

# --------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------

def dar_voto(request, Nombre):

    juego_pedido = Pedido.objects.get(Nombre_pedido = Nombre)
    total_votos = votos.objects.all()
    user_nombre = request.POST["usuario_nombre"]
    user_id = request.POST["usuario_id"] 

    hoy = timezone.now()
    
    for i in total_votos:

        fecha_voto = i.Ultimo_voto.date()
        
        if i.Usuario_id == user_id:
            
            if fecha_voto != hoy.date():
            
                juego_pedido.Numero_pedido += 1
                juego_pedido.save()
                i.Votos += 1
                i.save()
                mensaje_pedido = "Gracias por tu voto gamer"
                return render(request, "pedidos/pedidos.html", {"Mensaje" : mensaje_pedido})
            
            else:
                
                mensaje_pedido = "No puedes votar mas de una vez por dia"
                return render(request, "pedidos/pedidos.html", {"Mensaje" : mensaje_pedido})

    juego_pedido.Numero_pedido += 1
    juego_pedido.save()   
    registro_voto = votos.objects.create(Usuario_Nombre = user_nombre, Usuario_id = user_id, Votos = 1)

    mensaje_pedido = "Gracias por tu voto gamer"

    return render(request, "pedidos/pedidos.html", {"Mensaje" : mensaje_pedido})