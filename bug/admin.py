from django.contrib import admin
from bug.models import Categoria, Tipo, EstadoBug, Bug
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nome',)

class BugAdmin(admin.ModelAdmin):
    list_display=('autor','titulo','estado','categoria','dataPublicacao')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(EstadoBug)
admin.site.register(Tipo)
admin.site.register(Bug,BugAdmin)