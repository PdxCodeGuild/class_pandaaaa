from django.urls import path
from .views import (
    PostListView,
    PostDeleteView,
    UserPostListView,
    )
from .import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-chirps'),
    path('post/<int:pk>/del/', PostDeleteView.as_view(), name='chirp-delete'),
]