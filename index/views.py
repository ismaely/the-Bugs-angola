from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.urls import reverse, path
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.conf import settings
from utilizador.forms import LoginForm
from utilizador.models import Utilizador
from bug.models import Categoria, Tipo, EstadoBug, Bug




def internacional(request):
    context = {}
    return render(request, 'index/internacional.html',context)

    
def detail(request, slug):
    resp = Bug.objects.get(slug=slug)
    context = {'resp':resp} 
    return render(request, 'index/detalhe.html', context)


# the method that will list all soluction in system
def soluction(request):
    resp = Bug.objects.select_related('tipo').filter(tipo=4)
    context = {'lista':resp} 
    return render(request, 'index/soluction.html', context)


def index(request):
    lista = Bug.objects.select_related('estado').all().order_by('-created')
    context = {'lista': lista}
    return render(request, 'index/index.html', context)


def about(request):
    context = {}
    return render(request, 'index/about.html', context)


def contact(request):
    context = {}
    return render(request, 'index/contact.html', context)


def termsOfUse(request):
    context = {}
    return render(request, 'index/termsOfUse.html', context)


def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        try:
            if form.is_valid():
                senha = form.cleaned_data.get('password')
                nome = form.cleaned_data.get('username')
                resp = User.objects.get(username=nome)
                password = check_password(senha, resp.password)
                if resp.username == nome and password:
                    #conta = Utilizador.objects.get(user_id=resp.id)
                    if resp.is_active:
                        user = authenticate(username=nome,password=senha)
                        login(request, user)
                        #request.session.set_expiry(31000)
                        return HttpResponseRedirect(reverse('bug:home'))
                messages.warning(request, 'Dados da conta errado')
        except User.DoesNotExist:
            messages.warning(request, 'A conta não existe..')
    else:
        form = LoginForm(request.POST or None)
    context = {'form':form,}
    return render (request, 'utilizador/login.html', context)