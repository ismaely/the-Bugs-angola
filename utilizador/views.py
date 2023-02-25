from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.urls import reverse, path
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.conf import settings
from utilizador.forms import CategoriaForm
from utilizador.models import Utilizador


@login_required
def add_categoria(request):
    form = CategoriaForm(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                user = Group.objects.create_group(name=request.POST['nome'])
                form.save()
                form = CategoriaForm()

        except Exception as e:
           messages.warning(request, 'A conta não existe..')

    context = {'form': form}
    return render(request, 'utilizador/add_categoria.html', context)


@login_required
def newUser(request):
    form = UtilizadorConta_Form(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                user = User.objects.create_user(
                    username=request.POST['nome_utilizador'], last_name=request.POST['categoria'], email=request.POST['email'], password=SENHA_PADRAO)
                resp = form.save(commit=False)
                resp.user_id = user.id
                resp.estado = 0
                resp.save()
                return HttpResponseRedirect(reverse('secretaria:registar-utilizador'))

        except Exception as e:
            sweetify.error(
                request, 'Já existe um utilizador com este nome de Utilizador!.', persistent='OK', timer='3100')

    context = {'form': form}
    return render(request, 'utilizador/registar_utilizador.html', context)



# def to logout in system
def logoutUser(request):
    logout(request)
    return redirect('/')