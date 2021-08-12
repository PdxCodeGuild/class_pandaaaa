from django.http import request
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.models import User
# Generic View Classes
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
# Custom Models/Forms
from blog_app.models import BlogPost
from .forms import LoginForm, BlogPostForm

# Create your views here.
class Index(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        posts = BlogPost.objects.all()
        print(posts)
        return render(request,'index.html', {'posts':posts})

class Register(CreateView):
    model = User
    template_name = 'register.html'
    form_class = LoginForm
    def get_success_url(self):
        return reverse_lazy('index')

class Login(LoginView):
    template_name = 'login.html'

class Logout(LogoutView):
    template_name = 'logout.html'

class Profile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile.html'

class CreatePost(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'post.html'
    def get_success_url(self):
        return reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user

class EditPost(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'post.html'
    def get_success_url(self):
        return reverse_lazy('index')

    

