from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EstadoBug(models.Model):
    estado = models.CharField(max_length=150)
    def __str__ (self):
        return "%s" % (self.estado)


class Categoria(models.Model):
    nome = models.CharField(max_length=150)
    def __str__ (self):
        return "%s" % (self.nome)


class Tipo(models.Model):
    nome = models.CharField(max_length=150)
    def __str__ (self):
        return "%s" % (self.nome)



class Imagem(models.Model):
    titulo = models.CharField(max_length=170, blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)
    arquivos = models.FileField(upload_to="uploads/%Y/")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.id
