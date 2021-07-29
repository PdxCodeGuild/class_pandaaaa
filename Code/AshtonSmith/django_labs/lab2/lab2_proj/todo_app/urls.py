from django.urls import path
from . import views

app_name = 'todo_app'
urlpatterns = [
    path('', views.home, name= 'home'),
    path('add/', views.add, name= 'add'),
    path('delete/<int:pk>/' ,views.delete, name= 'delete')
]