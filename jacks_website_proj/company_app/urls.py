from django.urls import path
from . import views

# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('user/login', views.login),
    path('user/register', views.register),
    path('home', views.home),
    path('programs', views.programs),
]