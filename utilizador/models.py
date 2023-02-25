from django.db import models
from django.contrib.auth.models import User


class Genero(models.Model):
    nome = models.CharField(max_length=15)
    sigla = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return "%s" % (self.nome)




# Model for User
class Utilizador(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, parent_link=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, parent_link=True)
    data_nascimento=models.DateField(blank=True, null=True)
    ndi = models.CharField(max_length=40,blank=True, null=True)
    telefone = models.CharField(max_length=50,blank=True, null=True)
    foto = models.ImageField(upload_to='uploads/%d-%m-%y/', blank=True, null=True, default="user.jpg")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return '%d' % (self.id)