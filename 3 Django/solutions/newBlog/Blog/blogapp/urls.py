from django.urls import path 
from . import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.register, name="register"),
    path('create/', views.create, name="create"),
    #creating routes with unique identifiers, pk == id
    path('profile/<int:pk>', views.profile, name="profile"),
    path('edit/<int:id>', views.edit_post, name="edit"),
]
# ex. of how to pass param to route:
# {% url 'profile' user.id %}