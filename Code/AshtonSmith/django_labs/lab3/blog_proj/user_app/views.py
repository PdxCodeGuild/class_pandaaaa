from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, UpdateView
from .forms import RegisterForm, UpdateForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from blog_app.models import BlogPost
from django.views.generic.list import ListView


class LoginView(LoginView):
    template_name= 'user_app/login.html'



class LogoutView(LogoutView):
    template_name= 'user_app/logout.html'



class ProfileView(ListView):
    model = BlogPost
    template_name= 'user_app/profile.html'
    paginate_by = 5
    def get_queryset(self, **kwargs):
        user_id = self.kwargs['pk']
        return BlogPost.objects.filter(user= user_id)
    



class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'user_app/register.html'
    def get_success_url(self):
        return reverse_lazy('user_app:login')

class UpdateView(UpdateView):
    model = User
    form_class = UpdateForm
    # form_class = UpdateForm
    template_name = 'user_app/update.html'
    def get_success_url(self):
        return reverse_lazy('blog_app:home')
    # def get_queryset(self, **kwargs):
    #     user_id = self.kwargs['pk']
    #     return BlogPost.objects.filter(user= user_id)
