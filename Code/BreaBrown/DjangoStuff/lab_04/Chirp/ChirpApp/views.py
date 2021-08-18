from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post 

class ChirpPostList(ListView):
    model = Post
    template_name = 'home.html'


class ChirpPostDetail(DetailView):
    model = Post
    template_name = 'postdetails.html'

class CreateChirpPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditPost(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['body']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('ChirpApp:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author