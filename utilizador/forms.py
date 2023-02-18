from django import forms
from django.forms import ModelForm


class LoginForm(forms.Form):
    email = forms.CharField(max_length=80, widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder':'Enter a valid email address'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg','placeholder':'Enter password' }))
