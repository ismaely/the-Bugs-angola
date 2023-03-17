from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import date
import random, base64
# Create your models here.


class EstadoBug(models.Model):
    estado = models.CharField(max_length=150)
    def __str__ (self):
        return '%s' % self.estado


class Categoria(models.Model):
    nome = models.CharField(max_length=150)
    def __str__ (self):
        return '%s' % self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=150)
    def __str__ (self):
        return '%s' % self.nome


class Bug(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.PROTECT, parent_link=True)
    estado = models.ForeignKey(EstadoBug, on_delete=models.PROTECT, parent_link=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, parent_link=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING, parent_link=True)
    dataPublicacao = models.DateField()
    descricao = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=400,null=True, blank=True)
    #imagem = models.ImageField(upload_to="imagem/%d-%m-%yyyy/", blank=True, null=True)

    class Meta:
        ordering = ['-created']

    def __str__ (self):
        return '%d' % self.id
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo+'-'+str(date.today())+'-'+str(random.random()))
        super(Bug, self).save(*args, **kwargs)


class Imagem(models.Model):
    titulo = models.CharField(max_length=170, blank=True, null=True)
    content = models.TextField()
    arquivos = models.FileField(upload_to="uploads/%d-%m-%yyyy/",blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    dataPublicacao = models.DateField(default=date.today())
    slug = models.SlugField(max_length=400,null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING, parent_link=True, blank=True, null=True)

    def __str__ (self):
        return '%d' % self.id

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo+'-'+str(date.today())+'-'+str(random.random()))
        super(Imagem, self).save(*args, **kwargs)
