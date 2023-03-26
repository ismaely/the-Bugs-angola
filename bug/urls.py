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
    path('update_bug/<int:pk>/', views.update_bug, name="update-bug"),
    path('detail/<slug:slug>/', views.get_detail, name="detail"),
    path('get_search/', views.get_search, name="get-search"),
]