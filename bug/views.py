from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
# Create your views here.

@login_required
def home(request):
    context = {}
    return render (request, 'bug/home.html', context)



@login_required
def add_new_bug(request):
    if request.method == 'POST':
        form = Utilizador_Form(request.POST,request.FILES or None)
        try:
            if form2.is_valid() and form.is_valid():
                username = form2.cleaned_data['username']
                first_name = form2.cleaned_data['first_name']
                resp = form.save(commit=False)
                resp.user_id = user.id
                resp.save()
                form = Utilizador_Form()
                messages.success(request, 'Conta do utilizador criado com sucesso')
        except Exception as e:
                messages.warning(request, 'A conta de utilizador já existe com este username')
    else:
        form = Utilizador_Form(request.POST or None)
        form2 = User_Form(request.POST or None)

    context = {'form': form,'form2': form2}
    return render(request, 'utilizador/add_newUser.html', context)

