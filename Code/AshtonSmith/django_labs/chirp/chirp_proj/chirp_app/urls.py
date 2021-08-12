from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views
from .views import homeview
from django.conf.urls.static import static
from django.conf import settings 
# app_name = 'musicapp'
urlpatterns = [
    path('',homeview ,name= 'home' ),

]
# http://127.0.0.1:8000/api_radio_tracks/37151

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)