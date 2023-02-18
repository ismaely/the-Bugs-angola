from django.urls import path
from django.conf import settings
from . import views

app_name = 'utilizador'
urlpatterns = [
    path('loginUser/', views.loginUser, name="loginUser"),
]
