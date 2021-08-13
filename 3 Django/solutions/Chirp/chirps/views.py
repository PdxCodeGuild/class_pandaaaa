from .models import Chirp
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import CustomUser


PAGINATION_COUNT = 3

class PostListView(ListView):
    model = Chirp
    template_name = 'home.html'
    context_object_name = 'chirps'
    ordering = ['-date_posted']
    paginate_by = PAGINATION_COUNT

    def get_queryset(self):
        user = self.request.user
        follows = [user]
        return Chirp.objects.filter(author__in=follows).order_by('-date_posted')

class UserPostListView(ListView):
    model = Chirp
    template_name = 'chirps/user_posts.html'
    context_object_name = 'posts'
    paginate_by = PAGINATION_COUNT

    def visible_user(self):
        return get_object_or_404(CustomUser, username=self.kwargs.get('username'))
   

class PostDeleteView(DeleteView):
    model = Chirp
    template_name = 'chirps/post_delete.html'
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        return is_users(self.get_object().author, self.request.user)

