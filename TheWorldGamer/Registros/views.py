from django.shortcuts import render, redirect
from Juegos.models import Juego
from .models import Registro

from datetime import datetime
from datetime import timedelta
from django.utils import timezone

def agregar_valor(request, id):
    
    registros = Registro.objects.all()
    juegos = Juego.objects.all()
    game = Juego.objects.get(id = id)

    nombre = game.Nombre
    seccion = game.Seccion
    img = game.Imagen
    precio = request.POST["precio_confirmar"]
    tiempo = request.POST["tiempo_confirmar"]
    usuario = request.POST["usuario"]
    usuario_id = request.POST["usuario_id"]

    for i in registros:

        limite_7_dias = i.actualizacion.date() + timedelta(days=7)
        limite_15_dias = i.actualizacion.date() + timedelta(days=15)
        limite_1_mes = i.actualizacion.date() + timedelta(days=30)
        limite_3_meses = i.actualizacion.date() + timedelta(days=90)
        limite_6_meses = i.actualizacion.date() + timedelta(days=180)
        limite_1_año = i.actualizacion.date() + timedelta(days=365)
        
        hoy = timezone.now()

        if i.Id_usuario == usuario_id:

            if i.Juego == nombre:

                if i.Tiempo == "7 dias":

                    if hoy.date() > limite_7_dias:

                        i.Precio = precio
                        i.alquiladas += 1
                        i.Tiempo = tiempo
                        i.save()
                        Mensaje_alquilado = "El juego se ha alquilado exitosamente"
                        return render(request, "juegos/juegos.html", {"juegos" : juegos, "alquilado" : Mensaje_alquilado })
                    
                    else: 

                        Mensaje_no_alquilado = "Debes esperar hasta despues de el {} para poder volver a alquilar este juego".format(limite_7_dias)
                        return render(request, "juegos/juegos.html", {"juegos" : juegos, "alquilado" : Mensaje_no_alquilado })
                    
                if i.Tiempo == "15 dias":

                    if hoy.date() > limite_15_dias:

                        i.Precio = precio
                        i.alquiladas += 1
                        i.Tiempo = tiempo
                        i.save()
                        Mensaje_alquilado = "El juego se ha alquilado exitosamente"
                        return render(request, "juegos/juegos.html", {"juegos" : juegos, "alquilado" : Mensaje_alquilado })
                    
                    else: 

                        Mensaje_no_alquilado = "Debes esperar hasta despues de el {} para poder volver a alquilar este juego".format(limite_15_dias)
                        return render(request, "juegos/juegos.html", {"juegos" : juegos, "alquilado" : Mensaje_no_alquilado })
                    
                if i.Tiempo == "1 mes":

                    if hoy.date() > limite_1_mes:

                        i.Precio = precio
                        i.alquiladas += 1
                        i.Tiempo = tiempo
                        i.save()
                        Mensaje_alquilado = "El juego se ha alquilado exitosamente"
                        return render(request, "juegos/juegos.html", {"juegos" : juegos, "alquilado" : Mensaje_alquilado })
                    
                    else: 

                        Mensaje_no_alquilado = "Debes esperar hasta despues de el {} para poder volver a alquilar este juego".format(limite_1_mes)
                        return render(request, "juegos/juegos.html", {"juegos" : juegos, "alquilado" : Mensaje_no_alquilado })
                    
                if i.Tiempo == "3 meses":

                    if hoy.date() > limite_3_meses:

                        i.Precio = precio
                        i.alquiladas += 1
                        i.Tiempo = tiempo
                        i.save()
                        Mensaje_alquilado = "El juego se ha alquilado exitosamente"
                        return render(request, "juegos/juegos.html", {"juegos" : juegos, "alquilado" : Mensaje_alquilado })
                    
                    else: 

                        Mensaje_no_alquilado = "Debes esperar hasta despues de el {} para poder volver a alquilar este juego".format(limite_3_meses)
                        return render(request, "juegos/juegos.html", {"juegos" : juegos, "alquilado" : Mensaje_no_alquilado })
                    
                if i.Tiempo == "6 meses":

                    if hoy.date() > limite_6_meses:

                        i.Precio = precio
                        i.alquiladas += 1
                        i.Tiempo = tiempo
                        i.save()
                        Mensaje_alquilado = "El juego se ha alquilado exitosamente"
                        return render(request, "juegos/juegos.html", {"juegos" : juegos, "alquilado" : Mensaje_alquilado })
                    
                    else: 

                        Mensaje_no_alquilado = "Debes esperar hasta despues de el {} para poder volver a alquilar este juego".format(limite_6_meses)
                        return render(request, "juegos/juegos.html", {"juegos" : juegos, "alquilado" : Mensaje_no_alquilado })
                    
                if i.Tiempo == "1 año":

                    if hoy.date() > limite_1_año:

                        i.Precio = precio
                        i.alquiladas += 1
                        i.Tiempo = tiempo
                        i.save()
                        Mensaje_alquilado = "El juego se ha alquilado exitosamente"
                        return render(request, "juegos/juegos.html", {"juegos" : juegos, "alquilado" : Mensaje_alquilado })
                    
                    else: 

                        Mensaje_no_alquilado = "Debes esperar hasta despues de el {} para poder volver a alquilar este juego".format(limite_1_año)
                        return render(request, "juegos/juegos.html", {"juegos" : juegos, "alquilado" : Mensaje_no_alquilado })
    
    videojuego = Registro.objects.create(Usuario = usuario, Id_usuario = usuario_id, Juego = nombre, Seccion = seccion, Img = img, Precio = precio, Tiempo = tiempo, alquiladas = 1)
    
    Mensaje_alquilado = "El juego se ha alquilado exitosamente"
    
    return render(request, "juegos/juegos.html", {"juegos" : juegos, "alquilado" : Mensaje_alquilado })


