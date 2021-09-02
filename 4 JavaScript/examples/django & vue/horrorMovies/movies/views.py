from django.shortcuts import render, redirect

from .models import Villain, Movie
# Create your views here.
def home(request):
    return render(request, 'movies/home.html')

def list_view(request):
    villains = Villain.objects.all()
    movies = Movie.objects.all()
    context = {
        'movies': movies,
        'villains': villains
    }
    return render(request, 'movies/list.html', context)

def add_movie(request):
    if request.method =='GET':
        movies = Movie.objects.all()
        context = {
            'movies': movies
        }
        return render(request, 'movies/add_movie.html', context)

    elif request.method == 'POST':
        title = request.POST['title']
        starRating = request.POST['starRating']
        newVillain = Movie.objects.create(
            title = title, 
            starRating = starRating, 
        )
        return redirect('list_view')
    return render(request, 'movies/add_movie.html')

def add_villain(request):
    if request.method =='GET':
        movies = Movie.objects.all()
        context = {
            'movies': movies
        }
        return render(request, 'movies/add_villain.html', context)
    elif request.method == 'POST':
        name = request.POST['name']
        image = request.POST['image']
        newVillain = Villain.objects.create(
            name = name, 
            image = image, 
        )
        return redirect('list_view')