from django.http.response import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    # print(request.user.userprofile.avatar.url)
    return render(request, 'blog_app/home.html')


