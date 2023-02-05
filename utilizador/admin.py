from django.contrib import admin
from utilizador.models import Genero, Categoria, Utilizador

# Register your models here.

class UtilizadorAdmin(admin.ModelAdmin):
    list_display=('user', 'categoria', 'genero', 'data_nascimento','ndi','telefone')
    ordering = ['created']


class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nome', 'sigla')
    search_fields = ['nome']

admin.site.register(Genero)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Utilizador, UtilizadorAdmin)