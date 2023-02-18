from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.urls import reverse, path
from django.contrib import messages
from django.http import HttpResponseRedirect
from utilizador.forms import LoginForm
from utilizador.models import Utilizador




def loginUser(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                senha = form.cleaned_data.get('password')
                nome = form.cleaned_data.get('email')
                resp = User.objects.get(email=nome)
                password = check_password(senha, resp.password)
                if resp.email == nome and password:
                    #conta = Utilizador.objects.get(user_id=resp.id)
                    if resp.is_active:
                        user = authenticate(email=nome, password=senha)
                        login(request, user)
                        #request.session.set_expiry(31000) # a session vai terminar em 24 horas
                        return HttpResponseRedirect(reverse('bug:home'))
                    else:
                        return HttpResponseRedirect(reverse('utilizador:sair'))
               
        except User.DoesNotExist:
            messages.warning(request, 'A conta não existe...')

    context = {'form':form}
    return render (request, 'utilizador/login.html', context)
