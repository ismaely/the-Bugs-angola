from django import template
from django.contrib.auth.models import AbstractUser, User, Group
from utilizador.models import Utilizador

register = template.Library()

@register.simple_tag
def categoriaUser(idDuser):
    user = User.objects.get(id=idDuser)

    return ''