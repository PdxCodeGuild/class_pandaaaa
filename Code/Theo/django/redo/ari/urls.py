from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
# import views

urlpatterns = [
    path('',views.index, name='index'),
    path('results/<int:id>.html', views.results, name='results'),
]
