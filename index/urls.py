from django.urls import path
from django.conf import settings
from . import views

app_name = 'index'
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('termsOfUse/', views.termsOfUse, name="termsOfUse"),
    path('loginUser/', views.loginUser, name="loginUser"),
    path('detail/<int:pk>/', views.detail, name="detail"),
  
]
