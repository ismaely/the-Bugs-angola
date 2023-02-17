from django.shortcuts import render
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
    context = {}
    return render(request, 'index/login.html', context)