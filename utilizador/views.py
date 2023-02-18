from django.shortcuts import render
from utilizador.forms import LoginForm

# Create your views here.


def loginUser(request):
    context = {}
    return render (request, 'utilizador/login.html', context)
