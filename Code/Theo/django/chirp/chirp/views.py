from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView
from .models import Cheep

# Create your views here.

class Index(ListView):
    model = Cheep
    template_name = 'index.html'