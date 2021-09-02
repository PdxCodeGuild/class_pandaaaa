from django.urls import path
from . import views
from myproject import settings
from django.conf.urls.static import static
# from django.views.generic import Todo

app_name = 'user_app'
urlpatterns = [
    path('', views.home, name='home'),
    # path('loginfunc/', views.loginfunc, name='loginfunc'),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    # path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
    # path('register/', views.RegisterView.as_view(), name='register'),
    # path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#
