from .views import LoginView, LogoutView, PostDetailView, RegisterView, HomeView,  ProfileView
from django.urls import path
urlpatterns = [
    path('',HomeView.as_view() ,name= 'home' ),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('register/', RegisterView.as_view(),name='register'),
    path('profile/<slug:slug>', ProfileView.as_view(), name='profile'),
    path('post_detailed/<slug:slug>', PostDetailView.as_view(),name='detailed'),
]
