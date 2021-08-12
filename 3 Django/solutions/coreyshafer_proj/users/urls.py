from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLogin, register

urlpatterns= [
    #add URLS here: 
        # logout view: ('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
        # login: CustomLogin.as_view()
        # register: views.register\
        # profile: views.profile
]