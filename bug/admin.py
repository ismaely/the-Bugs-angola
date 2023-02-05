from django.contrib import admin
from bug.models import Categoria, Tipo, EstadoBug
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nome',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(EstadoBug)
admin.site.register(Tipo)