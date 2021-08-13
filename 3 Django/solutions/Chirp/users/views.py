# from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.shortcuts import redirect, render

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import CustomUser
from .forms import NewUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import get_user_model
User = get_user_model()

class Register(View):

    def post(self, request):
        f = NewUserForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')

    def get(self, request):
        form = NewUserForm()
        return render(request, 'cadmin/register.html', {'form': form})

class Login(LoginView):
    template_name = 'accounts/login.html'
    
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

class UserLogout(LogoutView):
    template_name = 'registration/logout.html'

class Profile(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'