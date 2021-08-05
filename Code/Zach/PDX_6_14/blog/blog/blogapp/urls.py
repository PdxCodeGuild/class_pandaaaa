from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.myview, name='myview'),
    path('create/', views.create, name='create'),
    path('profile/<pk>', views.profile, name='profile'),
    path('delete/<pk>', views.delete, name='delete'),
    #path('edit/<pk>'. views.edit, name='edit')
]