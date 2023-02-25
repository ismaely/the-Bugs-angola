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




def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        try:
            if form.is_valid():
                senha = form.cleaned_data.get('password')
                nome = form.cleaned_data.get('email')
                resp = User.objects.get(email=nome)
                password = check_password(senha, resp.password)
                
                if resp.email == nome and password:
                    #conta = Utilizador.objects.get(user_id=resp.id)
                    user = authenticate(request,email=resp.email,password=senha)
                    if resp.is_active:
                        #login(request, user)
                        return redirect('bug:home')
                        #return HttpResponseRedirect(reverse('bug:home'))
                messages.warning(request, 'Dados da conta errado')
        except User.DoesNotExist:
            messages.warning(request, 'A conta não existe..')
    else:
        form = LoginForm(request.POST or None)
    context = {'form':form,}
    return render (request, 'utilizador/login.html', context)


# def to logout in system
def logoutUser(request):
    logout(request)
    return redirect('/')