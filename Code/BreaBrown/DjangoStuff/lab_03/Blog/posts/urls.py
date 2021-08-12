from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.BlogPostList.as_view(), name='home'),
    path('post/<int:pk>/', views.BlogPostDetail.as_view(), name='detail'),
    path('post/new/', views.CreateBlogPost.as_view(), name='new'),
    path('post/<int:pk>/edit/', views.EditPost.as_view(), name='edit'),
    path('post/<int:pk>/delete/', views.DeletePost.as_view(), name='delete'),
]