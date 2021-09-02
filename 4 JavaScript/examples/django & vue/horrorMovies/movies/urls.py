from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list', views.list_view, name='list_view'),
    path('add_movie', views.add_movie, name="add_movie"),
    path('add_villain', views.add_villain, name="add_villain")

]
