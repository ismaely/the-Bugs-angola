from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .forms import BugForm
# Create your views here.

@login_required
def home(request):
    context = {}
    return render (request, 'bug/home.html', context)



@login_required
def add_new_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST,request.FILES or None)
        try:
            if form.is_valid():
                resp = form.save(commit=False)
                resp.save()
                form = BugForm()
                messages.success(request, 'Criado com sucesso')
        except Exception as e:
                messages.warning(request, 'já existe')
    else:
        form = BugForm(request.POST or None)
       

    context = {'form': form}
    return render(request, 'bug/add_new_bug.html', context)

