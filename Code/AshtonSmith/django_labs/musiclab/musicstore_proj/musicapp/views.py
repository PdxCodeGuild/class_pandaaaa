from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Album , Song , Artist
from .api import request_artist, request_data, request_list, request_radio, request_search
from django.shortcuts import render

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

def chartview(request):
    context = {'data':request_data()}
    return render(request, 'musicapp/api.html', context)

def api_artist(request, slug):
    my_dat = request_artist(slug)
    context = {'data':my_dat,
    'songs':request_list(my_dat['tracklist'])}
    return render(request, f'musicapp/api_artist.html', context)

def api_search(request):
    my_dat = request_search(request.GET['Search'])
    context = {'data':my_dat['data'],}
    return render(request, 'musicapp/api_search.html', context)

def api_radio(request):
    context = {'data': request_radio()}
    return render(request, 'musicapp/api_radio.html', context)