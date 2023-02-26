from django import forms
from django.forms import ModelForm
from utilizador.models import Utilizador


class LoginForm(forms.Form):
    username = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder':'Enter a valid username'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg','placeholder':'Enter password' }))


class CategoriaForm(forms.Form):
    nome= forms.CharField(max_length=80, min_length=4, widget=forms.TextInput(attrs={'class': 'form-control'}))



class Utilizador_Form(ModelForm):
    data_nascimento = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    ndi  = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(max_length=18, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Utilizador
        fields = ['genero', 'data_nascimento','ndi', 'telefone']
        widgets = {
            'genero': forms.Select(attrs={'class': 'form-control'}),
        }


class User_Form(forms.Form):
    #password = forms.CharField(max_length=25, required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=80, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    full_name = forms.CharField(max_length=180, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=60, required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
