from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render (request, 'bug/home.html', context)