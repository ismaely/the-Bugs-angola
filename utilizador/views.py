from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.urls import reverse, path
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from AOBug.settings import env
from utilizador.forms import CategoriaForm, Utilizador_Form, User_Form
from utilizador.models import Utilizador


@login_required
def add_categoria(request):
    form = CategoriaForm(request.POST or None)
    if request.method == 'POST':
        try:
            resp = Group.objects.get(name=request.POST['nome'])
            if resp is not None:
                messages.warning(request, 'A categoria já existe no sistema')
        except Group.DoesNotExist:
            if form.is_valid():
                Group.objects.create(name=request.POST['nome'])
                messages.success(request, 'Categoria criado com sucesso')
                form = CategoriaForm()
    
    context = {'form': form}
    return render(request, 'utilizador/add_categoria.html', context)



@login_required
def add_newUser(request):
    form = Utilizador_Form(request.POST or None)
    form2 = User_Form(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid() and form2.is_valid():
                username = form2.cleaned_data['username']
                full_name = form2.cleaned_data['full_name']
                email = form2.cleaned_data['email']
                user = User.objects.create_user(username=username, first_name=full_name,email=email, password=env('PASSWORD_PADRAO'))
                resp = form.save(commit=False)
                resp.user_id = user.id
                resp.save()
                form = Utilizador_Form()
                form2 = User_Form()
                messages.success(request, 'Categoria criado com sucesso')

        except Exception as e:
            messages.warning(request, 'A conta de utilizador já existe no sistema')

    context = {'form': form,'form2': form2}
    return render(request, 'utilizador/add_newUser.html', context)



# def to logout in system
def logoutUser(request):
    logout(request)
    return redirect('/')