from django import forms
from django.utils import timezone
from django.forms import ModelForm
from .models import Bug



class BugForm(ModelForm):
    autor = forms.CharField(max_length=14,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #descricao = forms.CharField(max_length=4500, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'id':'message'}))
    class Meta:
        model = Bug
        fields = ['titulo', 'estado', 'tipo', 'categoria', 'dataPublicacao', 'descricao','slug']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'dataPublicacao': forms.TextInput(attrs={'type':'date', 'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control html-editor', 'rows':'10', 'length': 4500})
        }