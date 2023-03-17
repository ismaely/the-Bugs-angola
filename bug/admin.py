from django.contrib import admin
from bug.models import Categoria, Tipo, EstadoBug, Bug, Imagem
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class BugAdmin(SummernoteModelAdmin):
    summernote_fields = ('descricao',)
    list_display=('autor','titulo','estado','categoria', 'tipo','dataPublicacao')

class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nome',)

class ImagemAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display=('titulo', 'arquivos')

admin.site.register(Tipo)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(EstadoBug)
admin.site.register(Bug, BugAdmin)
admin.site.register(Imagem,ImagemAdmin)
