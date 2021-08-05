from django.urls import path
from . import views
from django.urls.converters import register_converter

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='register'),    
]