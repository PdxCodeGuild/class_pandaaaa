from django.conf.urls import url
from django.contrib import admin
from .views import LoginView, LogoutView, PostDetailView, RegisterView, HomeView,  ProfileView
from django.urls import path, include
from . import views
from .views import homeview
from django.conf.urls.static import static
from django.conf import settings 
# app_name = 'chirp_app'
urlpatterns = [
    path('',HomeView.as_view() ,name= 'home' ),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('register/', RegisterView.as_view(),name='register'),
    path('profile/<slug:slug>', ProfileView.as_view(), name='profile'),
    path('post_detailed/<slug:slug>', PostDetailView.as_view(),name='detailed'),
]
# http://127.0.0.1:8000/api_radio_tracks/37151

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)