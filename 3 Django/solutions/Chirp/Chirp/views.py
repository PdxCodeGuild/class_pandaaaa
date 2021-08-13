from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from .models import Chirp
from users.models import CustomUser

# Create your views here.

class Index(ListView):
    model = Chirp
    template_name = 'index.html'

    def get_queryset(self):
        return Chirp.objects.all().order_by('-posted')

    def post(self, request):
        new_chirp = Chirp.objects.create(message=request.POST['text'], author=request.user)
        return redirect('index')


class ChirpDelete(DeleteView):
    model = Chirp
    template_name = 'chirp/post_delete.html'
    context_object_name = 'chirp'
    success_url = reverse_lazy('index')
    # def get_queryset(self):
    #     qs = super(ChirpDelete, self).get_queryset()
    #     return qs.filter(owner=self.request.user)
    
    # return redirect('home')

class Profile(ListView):
    # def get(self, request):
    #     print('hello')
    #     profile_author = CustomUser.objects.get(pk=self.kwargs.get('pk'))
    #     chirps = Chirp.objects.filter(author=profile_author).order_by('-date_posted')
    #     context = {
    #         'chirps' : chirps
    #     }
    #     return render(request, 'chirp/user_posts.html', context)
    model = Chirp
    template_name = 'chirp/user_posts.html'
    # context_object_name = 'chirps'

    # def get_context_data(self, **kwargs):
    #     print('GETTING context')


    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['chirps'] = Chirp.objects.filter(author=profile_author).order_by('-date_posted')

    #     return context
    def get_queryset(self):
        print('GETTING')
        # qs = super().get_queryset() 
        profile_author = CustomUser.objects.get(pk=self.kwargs.get('pk'))
        return Chirp.objects.filter(author=profile_author).order_by('-posted')
