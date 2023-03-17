from django import forms
from django.utils import timezone
from django.forms import ModelForm
from .models import Bug



class BugForm(ModelForm):
    autor = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control'}))
    autor = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control'}))
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
        }