# from django.http import request
from blog_app.models import BlogPost
from django.http import request
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .forms import LoginForm, BlogPostForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    return render(request,'index.html')

class Register(CreateView):
    model = User
    template_name = 'registerlogin.html'
    form_class = LoginForm
    def get_success_url(self):
        return reverse_lazy('index')

class Login(LoginView):
    template_name = 'registerlogin.html'

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
        return super(CreatePost, self).form_valid(form)

