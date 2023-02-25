from django.urls import path
from django.conf import settings
from . import views

app_name = 'index'
urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('termsOfUse/', views.termsOfUse, name="termsOfUse"),
    path('detail/<slug:slug>/', views.detail, name="detail"),
    path('soluction/', views.soluction, name="soluction"),
    path('internacional/', views.internacional, name="internacional"),
    path('loginUser/', views.loginUser, name="loginUser"),
    path('accounts/login/', views.loginUser, name='login'),
]
