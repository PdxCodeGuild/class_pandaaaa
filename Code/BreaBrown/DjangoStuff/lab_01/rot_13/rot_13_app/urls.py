from django.urls import path
from . import views

app_name = 'rot_13_app'

urlpatterns = [
    path('', views.index, name = 'index')
]
