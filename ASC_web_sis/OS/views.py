from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import ordens_servico,listadeprecos
from .forms import CadastroForm,ListaDePrecosForm
from docx import Document
 



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
        return redirect('tabela')

    else:
        Cadastro_pecasForm = ListaDePrecosForm
        cadastro = {
            'cadastro': Cadastro_pecasForm
        }
        return render(request, 'users/cadastropecas.html', context=cadastro)
    
def excluirpeca(request, id_peca):
    peca_a_excluir = listadeprecos.objects.get(pk=id_peca)
    if request.method == 'POST':
        peca_a_excluir.delete()
        return redirect('tabela')
    return render(request, 'users/exclusaopeca.html', {'item': peca_a_excluir})

def editarpeca(request, id_editar):
    ordemdeservico = listadeprecos.objects.get(pk=id_editar)

    if request.method == 'GET':
        formulario_cadastrade = ListaDePrecosForm(instance=ordemdeservico)
        return render(request,'users/cadastropecas.html', )
    else:
        formulario = ListaDePrecosForm(request.POST,instance=ordemdeservico)
        if formulario.is_valid():
            formulario.save()
        return redirect('tabela')
    
def osdetalhes(request):
    dados = {
        'dados': ordens_servico.objects.all()
    }
    return render(request, 'users/osdetalhes.html', context=dados)

def detalhescompletos(request, id_os_completa ):
    osdetalhe = {
        'osdetalhe': ordens_servico.objects.get(pk=id_os_completa)
    }
    return render(request,'users/detalhesoscompletas.html', context=osdetalhes)

def imprimiros(request, idos):
    sla = {
        'dados': ordens_servico.objects.get(pk=idos)
    }
<<<<<<< HEAD
    print(os_imprimir)

=======
    return render(request, 'users/osdetalhes.html', context=sla)
  
>>>>>>> e17ea1a0508b6de1defdd4b7c8e4125541def9e0
    


    