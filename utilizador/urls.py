from django.urls import path
from django.conf import settings
from . import views

app_name = 'utilizador'
urlpatterns = [
    path('logoutUser/', views.logoutUser, name="logoutUser"),
    path('adicionar_categoria/', views.add_categoria, name="add_categoria"),
    path('adicionarNovoUtilizador/', views.add_newUser, name="novo-utilizador"),

]
