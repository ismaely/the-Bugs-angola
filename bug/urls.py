from django.urls import path
from django.conf import settings
from . import views

app_name = 'bug'
urlpatterns = [
    path('home', views.home, name="home"),

]