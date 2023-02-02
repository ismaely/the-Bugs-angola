from django.shortcuts import render

# bug

def index(request):
   
    context = {}
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

# don't sleep