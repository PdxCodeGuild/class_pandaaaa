from django.urls import path
from . import views

app_name = 'phoneapp'
urlpatterns = [
    path('', views.myview, name='myview'),
    path('create/', views.mycreate, name='mycreate'),
    path('contact/<int:pk>', views.contact, name='contact'),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('delete/<int:pk>', views.delete, name="delete")
]