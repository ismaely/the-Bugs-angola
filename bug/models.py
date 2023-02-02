from django.db import models

# Create your models here.

class EstadoBug(models.Model):
    estado = models.CharField(max_length=150)
    def __str__ (self):
        return "%s" % (self.nome)



"""
class Bug(models.Model):
    titulo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    senha = models.CharField(max_length=170, blank=True, null=True)
    autor = models.CharField(max_length=170, blank=True, null=True)
    estado = models.ForeignKey(Tipologia, on_delete=models.CASCADE, parent_link=True)
    data = models.DateField()
    arquivo = models.FileField(upload_to="uploads/%Y/")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

   
    class Meta:
        ordering = ['titulo']
    def __str__ (self):
        return self.id

"""

class Imagem(models.Model):
    titulo = models.CharField(max_length=170, blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)
    data = models.DateField()
    estado = models.ForeignKey(EstadoBug, on_delete=models.CASCADE, parent_link=True)
    arquivos = models.FileField(upload_to="uploads/%Y/")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.id
