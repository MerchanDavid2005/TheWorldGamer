from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def entrada(request):

    return render(request, "inicio/entrada.html")

def inicio(request):

    return render(request, "inicio/inicio.html")

def yo(request):
    
    return render(request, "inicio/yo.html")

def contacto(request):

    return render(request, "inicio/contacto.html")

def enviar_correo(request):

    subject = request.POST["Usuario"] + " - " + request.POST["Asunto"]
    message = request.POST["Descripcion"]
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["DavidMerchan1203@gmail.com"]
    send_mail(subject, message, email_from, recipient_list)

    mensaje = "El envio se ha realizado exitosamente"

    return render(request, "inicio/contacto.html", {"Mensaje" : mensaje})


