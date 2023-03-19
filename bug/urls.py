from django.urls import path
from django.conf import settings
from . import views

app_name = 'bug'
urlpatterns = [
    path('home', views.home, name="home"),
    path('add_new_bug', views.add_new_bug, name="add-bug"),

]