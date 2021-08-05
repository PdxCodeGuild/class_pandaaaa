from django.urls import path
from . import views
# from django.views.generic import Todo

app_name = 'blog_app'
urlpatterns = [
    path('', views.home, name= 'home'),
    path('create/', views.CreatePost.as_view(), name='create'),
    path('list/', views.ListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
]





# from django.urls import path
# from . import views
# # from django.views.generic import Todo

# app_name = 'user_app'
# urlpatterns = [
#     # path('loginfunc/', views.loginfunc, name='loginfunc'),
#     path('login/', views.LoginView.as_view(), name= 'login'),
#     path('logout/', views.LogoutView.as_view(), name= 'logout'),
#     path('profile/<int:pk>', views.ProfileView.as_view(), name= 'profile'),
#     path('register/', views.RegisterView.as_view(), name= 'register'),
# ]