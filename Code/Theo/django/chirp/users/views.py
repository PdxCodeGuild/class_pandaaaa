from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic.edit import CreateView, UpdateView
# from django.views.generic.detail import DetailView
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



# Create your views here.
class Register(CreateView):
    model = CustomUser
    template_name = 'register.html'
    form_class = UserCreationForm
    
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

class Login(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

class Logout(LogoutView):
    template_name = 'logout.html'

class Profile(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'profile.html'
    form_class = UserChangeForm

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])

class PassChange(PasswordChangeView):
    model = CustomUser