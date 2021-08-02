from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.myview, name='myview'),
    path('index', views.index, name='index'),
    # path('create/', views.mycreate, name='mycreate'),
    # path('contact/<int:pk>', views.contact, name='contact'),
    # path('edit/<int:pk>', views.edit, name="edit"),
    # path('delete/<int:pk>', views.delete, name="delete")
]
