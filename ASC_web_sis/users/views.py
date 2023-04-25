from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from OS.models import ordens_servico
from OS.forms import CadastroForm



def novo_usuario(request):
    formulario = UserCreationForm()
    return render(request, 'users/register.html',{'formulario': formulario})

def pagina_inicial(request):
    dados = {
        'dados':ordens_servico.objects.all
    }

    return render(request, 'users/inicial.html', context=dados)

def novaos(request):
    CadastroForm = CadastroForm()
    formulario = {
        'formulario': CadastroForm
    }
    return render(request, 'users/novaos.html', context=formulario)

def osdetalhes(request,id_os):
    dados = {
        'test' : ordens_servico.objects.get(pk=id_os)
    }
    return render(request, 'users/osdetalhes.html')
