# from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import CustomUser
from .forms import RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Register(CreateView):
    model = CustomUser
    template_name = 'register.html'
    form_class = RegisterForm
    
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

class Login(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

class Logout(LogoutView):
    template_name = 'logout.html'

class Profile(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'profile.html'