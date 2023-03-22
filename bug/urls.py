from django.urls import path
from django.conf import settings
from . import views

app_name = 'bug'
urlpatterns = [
    path('home', views.home, name="home"),
    path('add_new_bug', views.add_new_bug, name="add-bug"),
    path('list_all_bug', views.list_all_bug, name="list-all-bug"),
    path('active_bug/<slug:slug>/', views.active_bug, name="active-bug"),
    path('disable_bug/<slug:slug>/', views.disable_bug, name="disable-bug"),

]