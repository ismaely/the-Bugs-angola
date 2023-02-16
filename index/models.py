from django.db import models
from django.template.defaultfilters import slugify
from datetime import date


# Create your models here.
class Internacional(models.Model):
    titulo = models.CharField(max_length=200)
    site = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    dataPublicacao = models.DateField()
    descricao = models.TextField()
    slug = models.SlugField(max_length=400,null=True, blank=True)
    imagem = models.ImageField(upload_to="imagem/%d-%m-%yyyy/", blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']

    def __str__ (self):
        return '%d' % self.id
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo+'-'+str(date.today()))
        elif not self.slug:
            self.slug = slugify(self.titulo+'-'+str(date.today()))

        super(Internacional, self).save(*args, **kwargs)