from django import forms
from django.utils import timezone
from django.forms import ModelForm
from .models import Bug, Arquivo



class BugForm(ModelForm):
    autor_id = forms.CharField(max_length=14,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #descricao = forms.CharField(max_length=4500, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'id':'message'}))
    class Meta:
        model = Bug
        fields = ['titulo', 'estado', 'tipo', 'categoria', 'dataPublicacao', 'descricao','slug']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'dataPublicacao': forms.TextInput(attrs={'type':'date', 'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control select2'}),
            'tipo': forms.Select(attrs={'class': 'form-control select2'}),
            'estado': forms.Select(attrs={'class': 'form-control select2'}),
            'slug': forms.TextInput(attrs={'class': 'form-control hidden'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control html-editor', 'rows':'10', 'length': 4500})
        }


class ArquivoForm(forms.ModelForm):
    bug_id = forms.CharField(max_length=6,required=False, widget=forms.TextInput(attrs={'class': 'form-control hidden'}))
    arquivo = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple':True, 'class': 'file-upload-default '}))
    class Meta:
        model = Bug
        fields = ['slug',  'arquivo']
        widgets = {
            'slug': forms.TextInput(attrs={'class': 'form-control hidden'}),
        }

# formulario para pesquisar consulta
class Search_Form(forms.Form):
    titulo = forms.CharField(max_length=180, widget=forms.TextInput(attrs={'class': 'form-control'}))
    