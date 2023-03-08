from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User, Group
from utilizador.models import Utilizador


class LoginForm(forms.Form):
    username = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder':'Enter a valid username'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg','placeholder':'Enter password' }))


class CategoriaForm(forms.Form):
    nome= forms.CharField(max_length=80, min_length=4, widget=forms.TextInput(attrs={'class': 'form-control'}))



class Utilizador_Form(ModelForm):
    data_nascimento = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    ndi  = forms.CharField(max_length=14, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'class': 'form-control'}))
    foto = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'hidden', 'class': 'form-control', 'id': 'fotoSalva'}))
    class Meta:
        model = Utilizador
        fields = ['genero', 'data_nascimento','ndi', 'telefone','foto']
        widgets = {
            'genero': forms.Select(attrs={'class': 'form-control'}),
        }


class User_Form(forms.Form):
    #password = forms.CharField(max_length=25, required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=80, min_length=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=180, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=60, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    def clean_usernmae(self):
        username =str(self.cleaned_data.get('username'))
        try:
            nome = User.objects.get(username=username)
            if nome.username == username:
                raise forms.ValidationError("O Username de utilizador já existe...!")
        except User.DoesNotExist:
            return username



CATEGORIA = Group.objects.all()
class Categoria_Privilegio_Form(forms.Form):
    categoria = forms.CharField(max_length=100, widget=forms.Select(choices=CATEGORIA, attrs={'class': 'form-control select2'}))
    permissao = forms.BooleanField(required=False, widget=forms.TextInput(attrs={'type':'checkbox', 'class': 'form-control' ,'id':'checkbox13'}))
    
    