from django.contrib import admin
from utilizador.models import Genero, Utilizador

# Register your models here.

class UtilizadorAdmin(admin.ModelAdmin):
    list_display=('user', 'genero', 'data_nascimento','ndi','telefone','estadoPassword')
    ordering = ['created']


class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nome', 'sigla')
    search_fields = ['nome']

admin.site.register(Genero)
admin.site.register(Utilizador, UtilizadorAdmin)