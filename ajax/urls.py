from django.urls import path
from django.conf import settings
from . import views

app_name = 'ajax'
urlpatterns = [
    path('remove_privilege_categoria/', views.remove_privilege_categoria, name="remove-privilege-categoria"),
]
