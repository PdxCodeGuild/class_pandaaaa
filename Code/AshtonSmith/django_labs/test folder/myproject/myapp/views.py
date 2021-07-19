from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def home(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    # return HttpResponse('<h1>hello world</h1>')
    return render(request, 'myapp/index.html', context)