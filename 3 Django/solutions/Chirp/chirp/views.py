from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView
from .models import Chirp

# Create your views here.

class Home(ListView):
    model = Chirp
    template_name = 'index.html'