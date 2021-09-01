from django.contrib import admin
from django.views.generic.base import TemplateView
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]