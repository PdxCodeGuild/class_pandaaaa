from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, PostForm, CommentForm
from .models import Post, CustomUser, Comment
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.http import Http404
from django.utils.translation import ugettext as _
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.db.models import F
# Create your views here.

def homeview(request):
    return render(request,'chirp_app/home.html')



class LoginView(LoginView):
    template_name= 'registration/login.html'



class LogoutView(LogoutView):
    template_name= 'registration/logout.html'



class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    def get_success_url(self):
        return reverse_lazy('login')



class ProfileView(ListView):
    template_name = 'chirp_app/profile.html'
    def get_queryset(self, *args, **kwargs):
        return  Post.objects.filter(author_id=self.kwargs ['slug'])



class HomeView(ListView):
    template_name ='chirp_app/home.html'
    context_object_name = 'home'
    model = Post


    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = PostForm()
        context['data'] = Post.objects.order_by('-posttime')
        context['comments'] = Comment.objects.all()
        return context


    def post(self, request):
        request.POST['text']
        newpost = Post.objects.create(text=request.POST['text'],author=request.user)
        newpost.save()
        return redirect('home')


class PostDetailView(ListView):
    template_name ='chirp_app/post_detail.html'
    my_post = None
    def get_queryset(self, *args, **kwargs):
        self.my_post = Post.objects.filter(id=self.kwargs['slug'])
        return self.my_post
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(post_id=self.kwargs['slug'])
        return context
    def post(self, request, slug, *args, **kwargs):
        self.get_queryset()
        newpost = Comment.objects.create(text=request.POST['text'],author=request.user,post=self.my_post[0])
        newpost.save()
        my_post = Post.objects.get(id=slug)
        my_post.comment_count += 1
        my_post.save()
        return redirect('home')