from django.urls import path
from . import views
# from django.views.generic import Todo

app_name = 'todo_app'
urlpatterns = [
    path('', views.home, name= 'home'),
    path('detailed/<int:pk>', views.TodoDetailed.as_view(), name= 'completed'),
    path('completed/detailed/<int:pk>', views.TodoDetailed.as_view(), name= 'completed'),

    path('medium/detailed/<int:pk>', views.TodoDetailed.as_view(), name= 'completed'),
    path('low/detailed/<int:pk>', views.TodoDetailed.as_view(), name= 'completed'),
    path('high/detailed/<int:pk>', views.TodoDetailed.as_view(), name= 'completed'),

    path('completed/', views.completed, name= 'completed'),
    path('add/', views.add, name= 'add'),
    path('edit/<int:pk>/', views.TodoUpdate.as_view(), name= 'edit'),

    path('completed/edit/<int:pk>/', views.TodoUpdate.as_view(), name= 'edit'),
    path('high/edit/<int:pk>/', views.TodoUpdate.as_view(), name= 'edit'),
    path('medium/edit/<int:pk>/', views.TodoUpdate.as_view(), name= 'edit'),
    path('low/edit/<int:pk>/', views.TodoUpdate.as_view(), name= 'edit'),

    path('delete/<int:pk>/' ,views.delete, name= 'delete'),
    
    path('high/delete/<int:pk>/' ,views.delete, name= 'delete'),
    path('medium/delete/<int:pk>/' ,views.delete, name= 'delete'),
    path('low/delete/<int:pk>/' ,views.delete, name= 'delete'),
    
    path('high/', views.high, name= 'high'),
    path('medium/', views.medium, name= 'medium'),
    path('low/', views.low, name= 'low'),
]