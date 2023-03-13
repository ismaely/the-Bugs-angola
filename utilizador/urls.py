from django.urls import path
from django.conf import settings
from . import views

app_name = 'utilizador'
urlpatterns = [
    path('logoutUser/', views.logoutUser, name="logoutUser"),
    path('adicionar_categoria/', views.add_categoria, name="add_categoria"),
    path('adicionarNovoUtilizador/', views.add_newUser, name="novo-utilizador"),
    path('list_users/', views.list_users, name="list-users"),
    path('profil_user/', views.profil_user, name="profil-user"),
    path('active_user/<int:pk>/', views.active_user, name="active-user"),
    path('disable_user/<int:pk>/', views.disable_user, name="disable-user"),
    path('reset_password/<int:pk>/', views.reset_password, name="reset-password"),
    path('set_category_privilege/', views.set_category_privilege, name="set-category-privilege"),
    path('list_group/', views.list_group, name="list-group"),
    path('set_user_groups/', views.set_user_groups, name="set-user-groups"),
    path('set_privileges_of_user/', views.set_privileges_of_user, name="set-privileges-user"),
    path('update_user/<slug:slug>/', views.update_user, name="update-user"),
    path('update_categoria/<int:pk>/', views.update_categoria, name="update-categoria"),
    path('show_privilege_categoria/<int:pk>/', views.show_privilege_categoria, name="show-privilege-categoria"),
    path('show_all_privilege_user/<int:pk>/', views.show_all_privilege_user, name="all-privilege-user"),
]
