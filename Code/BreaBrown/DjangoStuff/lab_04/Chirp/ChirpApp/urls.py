from django.urls import path

from . import views

app_name = 'ChirpApp'

urlpatterns = [
    path('', views.ChirpPostList.as_view(), name='home'),
    path('post/<int:pk>/', views.ChirpPostDetail.as_view(), name='detail'),
    path('post/new/', views.CreateChirpPost.as_view(), name='new'),
    path('post/<int:pk>/edit/', views.EditPost.as_view(), name='edit'),
    path('post/<int:pk>/delete/', views.DeletePost.as_view(), name='delete'),
]