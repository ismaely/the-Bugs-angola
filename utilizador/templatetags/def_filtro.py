from django import template
from django.contrib.auth.models import AbstractUser, User, Group
from utilizador.models import Utilizador
from django.http import HttpRequest

register = template.Library()



@register.simple_tag
def get_size_user(idGroup):
    qunt = User.objects.filter(groups=idGroup).count()
    return qunt



@register.simple_tag
def get_categoria_user(idDuser):
    name = ''
    grp = Group.objects.filter(user=idDuser)
    cont = 1
    for  gr in grp:
        if len(grp) > 1:
            if cont == 1:
                name = gr.name 
                cont +=1
            else:
                name = name +','+ gr.name
        else:
            return {'name': gr.name}
    return {'name':name}

