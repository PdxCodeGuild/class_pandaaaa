from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .models import Album, Playlist , Song , Artist, UserProfile
from .api import request_artist, request_data, request_list, request_radio, request_radio_tracks, request_search, request_song
from .yt_api import yt_search
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.views.generic import CreateView
from django.views.generic.base import View


class HomeView(ListView):
    model = UserProfile
    
    context_object_name = 'users'
    template_name = 'musicapp/home.html'
    def get_context_data(self, **kwargs):
        context = {'data':UserProfile.objects.order_by('-last_activity')}
        print(context)
        # super().get_context_data(**kwargs)
        return context

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
    my_data = request_radio()
    context = {'data': my_data}
    return render(request, 'musicapp/api_radio.html', context)


def api_radio_tracks(request, slug):
    my_dat = request_radio_tracks(slug)
    context = {'data': my_dat}
    return render(request, 'musicapp/api_radio_tracks.html',context)

def profile_view(request, slug):
    my_song_list = Playlist.objects.get(userprofile=slug)
    my_song_list = str(my_song_list).split(",")
    temp = []
    for i in my_song_list:
        temp.append(request_song(i)) 

    curr_user = UserProfile.objects.get(user_id=slug)
    context = {'data':temp,'my_user': curr_user}
    return render(request, 'musicapp/profile.html',context)

class LoginView(LoginView):
    template_name= 'registration/login.html'
class LogoutView(LogoutView):
    template_name= 'registration/logout.html'
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    def get_success_url(self):
        return reverse_lazy('login')

class LikeSong(View):
    def get(self,request, slug):
        context = {'data':request_data()}
        my_song_list = Playlist.objects.get(userprofile=request.user.id)
        # print(request.getHeader('referer'))
        if slug in str(my_song_list):
            pass
        else:
            temp = str(my_song_list) + ',' + str(slug)
            my_song_list.song_list = temp
            my_song_list.save()
        return render(request, 'musicapp/home.html', context)
# obj.save(update_fields=['field1', 'field2', ...])
    def post(self):
        return None

def songdetail_view(request,slug):
    song = request_song(slug)
    artist = song['artist']['name']
    song_title = song['title']
    data = yt_search(song_title + ' ' + artist)
    # print(data['items'][0]['id'])
    my_str = 'https://www.youtube.com/embed/' + data['items'][0]['id']['videoId']
    context = {'data': my_str ,
    'data2':song}
    return render(request, 'musicapp/song_detail.html', context)



        # profile = UserProfile.objects.get(user=request.user)
        # songs = profile.liked_songs
        # temp = profile.liked_songs.song_list + ',' + slug
        # profile.liked_songs.song_list = temp
        # # print(temp)
        # print('efore')
        # print(profile.liked_songs.song_list)
        # profile.liked_songs.save(update_fields = ['liked_songs'])
        # print('afrter')