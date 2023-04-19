from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def novo_usuario(request):
    formulario = UserCreationForm()
    return render(request, 'users/register.html',{'formulario': formulario})

def pagina_inicial(request):
    return render(request, 'users/inicial.html')



