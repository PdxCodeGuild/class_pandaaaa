from django.urls import path,include
from django.urls.converters import register_converter 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name="profile")
]