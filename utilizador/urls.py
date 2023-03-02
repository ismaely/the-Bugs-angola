from django.urls import path
from django.conf import settings
from . import views

app_name = 'utilizador'
urlpatterns = [
    path('logoutUser/', views.logoutUser, name="logoutUser"),
    path('adicionar_categoria/', views.add_categoria, name="add_categoria"),
    path('adicionarNovoUtilizador/', views.add_newUser, name="novo-utilizador"),
    path('list_users/', views.list_users, name="list-users"),
    path('profil_user/<slug:slug>/', views.profil_user, name="profil-user"),
    path('active_user/<int:pk>/', views.active_user, name="active-user"),
    path('disable_user/<int:pk>/', views.disable_user, name="disable-user"),
    path('reset_password/<int:pk>/', views.reset_password, name="reset-password"),
    path('set_category_privilege', views.set_category_privilege, name="set-category-privilege"),

]
