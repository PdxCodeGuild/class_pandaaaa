from django.contrib import admin
from django.urls import path
from . import views
app_name = 'phone_app'
urlpatterns = [
    path('', views.home, name='home' ),
    path('profile/<int:pk>', views.profile, name='profile'),
]
