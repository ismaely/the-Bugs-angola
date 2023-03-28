"""
@author [Gunza Ismael]
@email [7ilip@gmail.com]
@create date 2023-03-22 11:11:43
@modify date 2023-03-22 11:11:43
@desc [description]
 """

from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from datetime import date
from .forms import BugForm, ArquivoForm, Search_Form
from .models import Arquivo, Bug 
from AOBug.settings import env
import os



@login_required
def home(request):
    context = {}
    return render (request, 'bug/home.html', context)


#listar todos bugs, pertencente ao utilizador que criou
#@permission_required('polls.add_choice', login_url='/loginpage/')
@login_required
def list_all_bug(request):
    lista = Bug.objects.select_related('autor').filter(autor=request.user)
    context = {'lista': lista}
    return render(request, 'bug/list_all_bug.html', context)


#função para fazer consulta 
@login_required
def get_search(request):
    form = Search_Form(request.POST or None)
    if request.method == 'POST':
        lista = Bug.objects.filter(titulo__icontains=request.POST.get('titulo'))
        if len(lista) == 0:
            messages.warning(request,"Dados não encontrado")
        else:
            context = {'lista': lista}
            return render(request, 'bug/list_all_bug.html', context)
        
    context = {'form': form}
    return render(request, 'bug/search.html', context)


@login_required
def get_detail(request, slug):
    lista = get_object_or_404(Bug, slug=slug)
    arquivo = Arquivo.objects.filter(bug_id=lista.id)
    pdf = False
    imagem = False
    for res in arquivo:
        exten = res.arquivo.name.split('.')
        # verficar se é imagem 
        if exten[1] in env('EXSTENSAO'):
            imagem = True
        else:
            pdf = True
    context = {'lista': lista, 'arquivo': arquivo, 'pdf': pdf, 'imagem': imagem}
    return render(request, 'bug/detail.html', context)


# ativar publicação
@login_required
def active_bug(request, slug):
    bg = Bug.objects.get(slug=slug)
    bg.estado_id = 2
    bg.save()
    messages.success(request, 'Publicação ativada com sucesso')
    return HttpResponseRedirect(reverse('bug:list-all-bug'))
    

# função que vai desativar a publicação
@login_required
def disable_bug(request, slug):
    bg = Bug.objects.get(slug=slug)
    bg.estado_id = 3
    bg.save()
    messages.warning(request, 'Publicação desativada com sucesso')
    return HttpResponseRedirect(reverse('bug:list-all-bug'))


#atualizar dados do bug e o arquivo existente
@login_required
def update_bug(request, pk):
    bugs = Bug.objects.get(id=pk)
    arq = Arquivo.objects.filter(bug_id=pk)
    if request.method == 'POST':
        form = BugForm(request.POST)
        form2 = ArquivoForm(request.POST,request.FILES or None)
        try:
            if form.is_valid() and form2.is_valid():
                novo_arquivos = request.FILES.getlist('arquivo')
                data = form.cleaned_data
                
                # atualização dos dados do Bug
                data.update({'autor_id':request.user.id})
                for key, value in data.items():
                    setattr(bugs, key, value)
                bugs.save()

                # Remover arquivos antes de atualizar
                if len(novo_arquivos) != 0:
                    for dados in arq:
                        if len(dados.arquivo) > 0:
                            os.remove(dados.arquivo.path)

                arq.delete()
                for k in novo_arquivos:
                    novoArq = Arquivo.objects.create(bug_id=bugs.id, arquivo=k)

                messages.success(request, 'Informação atualizada com sucesso')
                return HttpResponseRedirect(reverse('bug:list-all-bug'))

        except Exception as e:
                messages.warning(request, 'Dados errados na atualização!')
    else:
        form = BugForm(request.POST or None, instance=bugs)
        form2 = ArquivoForm(request.POST,request.FILES or None)

    context = {'form': form, 'form2': form2, 'pk': pk}
    return render(request, 'bug/add_new_bug.html', context)



#registar uma nova falhas
@login_required
def add_new_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        form2 = ArquivoForm(request.POST,request.FILES or None)
        try:
            if form.is_valid() and form2.is_valid():
                arquivos = request.FILES.getlist('arquivo')
                resp = form.save(commit=False)
                resp.autor_id = request.user.id
                resp.save()
                for k in arquivos:
                    arq = Arquivo.objects.create(bug_id=resp.id, arquivo=k)
                form = BugForm()
                form2 = ArquivoForm()
                messages.success(request, 'Informação divulgada com sucesso')
        except Exception as e:
                messages.warning(request, 'Dados errados, falha interna!')
    else:
        form = BugForm(request.POST or None)
        form2 = ArquivoForm(request.POST,request.FILES or None)
       

    context = {'form': form, 'form2': form2}
    return render(request, 'bug/add_new_bug.html', context)

