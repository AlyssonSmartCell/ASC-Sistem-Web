from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import ordens_servico,listadeprecos
from .forms import CadastroForm,ListaDePrecosForm
 



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
    tabela = {
        'tabela': listadeprecos.objects.all()
    }
    return render(request, 'users/tabeladeprecos.html', context= tabela)

def garantia(request):
    return render(request, 'users/notadegarantia.html')

def excluir(request, cliente):
    osexcluir = ordens_servico.objects.get(pk=cliente)
    if request.method == 'POST':
        osexcluir.delete()
        return redirect('PaginaInicial')
    return render(request,'users/confirmar_exclusao.html', {'item': osexcluir})

def cadastropeças(request):
    if request.method == 'POST':
        a = ListaDePrecosForm(request.POST)
        if a.is_valid():
            a.save()
        return redirect('cadastropeças')

    else:
        Cadastro_pecasForm = ListaDePrecosForm
        cadastro = {
            'cadastro': Cadastro_pecasForm
        }
        return render(request, 'users/cadastropeças.html', context=cadastro)

    