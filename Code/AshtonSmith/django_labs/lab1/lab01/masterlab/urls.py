from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'masterlab'
urlpatterns= [
    path('', views.home, name ='home'),
    path('ari/', views.ari, name ='ari'),
    path('rps/', views.rps, name ='rps'),
    path('rot/', views.rot, name ='rot'),
    path('nump/', views.nump, name ='nump'),
    path('unit/', views.unit, name ='unit'),
]