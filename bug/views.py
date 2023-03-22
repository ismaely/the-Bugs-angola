from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from datetime import date
import random
from .forms import BugForm, ArquivoForm
from .models import Arquivo, Bug



@login_required
def home(request):
    context = {}
    return render (request, 'bug/home.html', context)


#@permission_required('polls.add_choice', login_url='/loginpage/')
@login_required
def list_all_bug(request):
    lista = Bug.objects.all()
    context = {'lista': lista}
    return render(request, 'bug/list_all_bug.html', context)


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

