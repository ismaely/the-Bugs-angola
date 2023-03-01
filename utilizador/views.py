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
from django.utils import timezone
import random, base64
from utilizador.forms import CategoriaForm, Utilizador_Form, User_Form
from utilizador.models import Utilizador



@login_required
def set_category_privilege(request):
    context = {}
    return render(request, 'utilizador/set_category_privilege.html')


@login_required
def list_users(request):
    list_user = Utilizador.objects.select_related('user').filter(user__is_superuser=False)
    #list_user = Utilizador.objects.all()
    context = {'lista': list_user}
    return render(request, 'utilizador/list_users.html', context)



@login_required
def profil_user(request, slug):
    #list_user = User.objects.select_related('user').filter(Q(estudante__pessoa__passaporte=bi) )
    list_user = User.objects.all()
    context = {'lista': list_user}
    return render(request, 'utilizador/profil_user.html', context)


#função que vai desativar a conta 
@login_required
def active_user(request, pk):
    if pk > 0:
        user = User.objects.get(id=pk)
        user.is_active = 1
        user.save()
        sweetify.success(
            request, 'Conta Ativado com sucesso!....', timer='4900', button='Ok')
        return HttpResponseRedirect(reverse('utilizador:listar_utilizador'))
    else:
        sweetify.info(request, 'Acesso Negado!Falha....',
                      timer='4900', button='Ok')
        return HttpResponseRedirect(reverse('utilizador:listar_utilizador'))



# função que vai desativar conta de utilizador
@login_required
def desativar_conta(request, pk):
    if pk > 0:
        user = User.objects.get(id=pk)
        user.is_active = 0
        user.save()
        sweetify.success(
            request, 'Conta Desativada com sucesso!....', timer='4900', button='Ok')
        return HttpResponseRedirect(reverse('utilizador:listar_utilizador'))
    else:
        sweetify.info(request, 'Acesso Negado!Falha....',
                      timer='4900', button='Ok')
        return HttpResponseRedirect(reverse('utilizador:listar_utilizador'))


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
    if request.method == 'POST':
        form = Utilizador_Form(request.POST,request.FILES or None)
        form2 = User_Form(request.POST)
        try:
            resp = User.objects.get(email=request.POST.get('email'))
            if resp is not None:
                messages.warning(request, 'O E-mail ja existe no sistema')
        except Exception as e:
            try:
                if form2.is_valid() and form.is_valid():
                    username = form2.cleaned_data['username']
                    full_name = form2.cleaned_data['full_name']
                    email = form2.cleaned_data['email']
                    user = User.objects.create_user(username=username, first_name=full_name,email=email, password=env('PASSWORD_PADRAO'))
                    resp = form.save(commit=False)
                    resp.user_id = user.id
                    resp.save()
                    form = Utilizador_Form()
                    form2 = User_Form()
                    messages.success(request, 'Conta do utilizador criado com sucesso')
            except Exception as e:
                messages.warning(request, 'A conta de utilizador já existe com este username')
    
    else:
        form = Utilizador_Form(request.POST or None)
        form2 = User_Form(request.POST or None)

    context = {'form': form,'form2': form2}
    return render(request, 'utilizador/add_newUser.html', context)



# função responsavel por tratar da foto 
@login_required
def prepara_foto(request):
    img = request.POST["foto"]
    nome = str(timezone.now()).split('.')
    foto = []
    inicio = img.find(',')
    imagem = img[inicio+1:]

    with open("./media/uploads/foto/"+ str(nome[0]) + "_" + str(random.random()) + ".png", "wb") as fh:
        fh.write(base64.b64decode(imagem))
        foto = str(fh).split('=')
        um = foto[1].replace(">", '')

    um = um.replace("'", '')
    um = um.split('media/')
    return um[1]


# def to logout in system
@login_required
def logoutUser(request):
    logout(request)
    return redirect('/')