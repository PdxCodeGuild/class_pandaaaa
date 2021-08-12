from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Album , Song , Artist
# Create your views here.

# def home(request):
#     return render(request,'musicapp/home.html')


class HomeView(ListView):
    model = Album 
    context_object_name = 'albums'
    template_name = 'musicapp/home.html'

class AlbumView(DetailView):
    model = Album
    context_object_name= 'album'
    template_name = 'musicapp/album_detail.html'

   
class SongView(DetailView):
    model = Song
    context_object_name= 'song'
    template_name = 'musicapp/song_detail.html' 


class ArtistView(DetailView):
    model = Artist 
    context_object_name= 'artist'
    template_name = 'musicapp/artist_detail.html' 

