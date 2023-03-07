from django.contrib import admin
from utilizador.models import Genero, Utilizador, Permissao_Nao_Visivel

# Register your models here.

class UtilizadorAdmin(admin.ModelAdmin):
    list_display=('user', 'genero', 'data_nascimento','ndi','telefone','estadoPassword')
    ordering = ['created']


class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nome', 'sigla')
    search_fields = ['nome']


class PermissaoN_VisivelAdmin(admin.ModelAdmin):
    list_display=('tipo', 'descricao')


admin.site.register(Permissao_Nao_Visivel,PermissaoN_VisivelAdmin)
admin.site.register(Genero)
admin.site.register(Utilizador, UtilizadorAdmin)