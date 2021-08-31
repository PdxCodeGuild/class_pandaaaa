from django.urls import path

from . import views

urlpatterns = [
    # render template
    path('', views.todo_list, name = 'list'),
    # get info
    path('get', views.todos, name='get'),
    # handle post
    path('add/', views.add_todo, name = 'add'),
    # handle delete
    path('delete/', views.delete_todo, name = 'delete'),
]
