from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import ordens_servico
from .forms import CadastroForm



# Create your views here.
def editar(request, id_os):
    ordemdeservico = ordens_servico.objects.get(pk=id_os)

    if request.method == 'GET':
        formulario_cadastrade = CadastroForm(instance=ordemdeservico)
        return render(request,'users/novaos.html', {'formulario':formulario_cadastrade})
    else:
        formulario = CadastroForm(request.POST,instance=ordemdeservico)
        if formulario.is_valid():
            formulario.save()
        return redirect('PaginaInicial')
    
def consultarprecos(request):
    return render(request, 'users/tabeladeprecos.html')

def garantia(request):
    return render(request, 'users/notadegarantia.html')



    