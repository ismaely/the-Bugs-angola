from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from datetime import date
import random
from .forms import BugForm, ArquivoForm
from .models import Arquivo, Bug

# Create your views here.

@login_required
def home(request):
    context = {}
    return render (request, 'bug/home.html', context)


#@permission_required('polls.add_choice', login_url='/loginpage/')
@login_required
def list_all_bug(request):
    lista = Arquivo.objects.all()
    context = {'lista': lista}
    return render(request, 'bug/list_all_bug.html', context)



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
                messages.success(request, 'Dados inserido com sucesso')
        except Exception as e:
                messages.warning(request, 'Dados errados, falha interna')
    else:
        form = BugForm(request.POST or None)
        form2 = ArquivoForm(request.POST,request.FILES or None)
       

    context = {'form': form, 'form2': form2}
    return render(request, 'bug/add_new_bug.html', context)

