from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages

# Create your views here.

class user_registro(View):
    
    def get(self, request):
        
        form = UserCreationForm()
        return render(request, "usuario/registrar.html", {"form" : form})
    
    def post(self, request):
        
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
        
            usuario = form.save()
            
            login(request, usuario)
            
            return redirect("Inicio")
        
        else:
            
            for msg in form.error_messages:
                
                messages.error(request, form.error_messages[msg])
            
            return render(request, "usuario/registrar.html", {"form" : form})
        
def cerrar_sesion(request):
        
    logout(request)
    return redirect("Inicio")

def iniciar_sesion(request):
    
    if request.method == "POST":
        
        form=AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username = nombre_usuario, password = password)
            
            if usuario is not None:
                
                login(request, usuario)
                return redirect ("Inicio")
            
            else:
                
                messages.error(request, "Este usuario no existe")
                
        else:
            
            messages.error(request, "Estos datos son incorrectos")
    
    form = AuthenticationForm()
    
    return render(request, "usuario/login.html", {"form" : form})
    
        
        