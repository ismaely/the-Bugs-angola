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




# def to logout in system
def logoutUser(request):
    logout(request)
    return redirect('/')