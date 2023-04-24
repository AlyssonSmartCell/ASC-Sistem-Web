from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def novo_usuario(request):
    formulario = UserCreationForm()
    return render(request, 'users/register.html',{'formulario': formulario})

def pagina_inicial(request):
    return render(request, 'users/inicial.html')

def novaos(request):
    return render(request, 'users/novaos.html')

def osdetalhes(request):
    return render(request, 'users/osdetalhes.html')
