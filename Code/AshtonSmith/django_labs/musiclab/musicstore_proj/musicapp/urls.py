
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views
from .views import HomeView, AlbumView, ArtistView, LikeSong, RegisterView, SongView, chartview, api_artist,api_search, api_radio, api_radio_tracks
from django.conf.urls.static import static
from django.conf import settings 
# app_name = 'musicapp'
urlpatterns = [
    path('',HomeView.as_view() ,name= 'home' ),
    path('album/<slug:pk>',AlbumView.as_view() ,name= 'album' ),
    path('song/<slug:pk>',SongView.as_view() ,name= 'song' ),
    path('artist/<slug:pk>',ArtistView.as_view() ,name= 'artist' ),
    path('api/', chartview, name= 'api'),
    path('api/<slug:slug>', api_artist ,name= 'api_artist'),
    path('api_search', api_search ,name= 'api_search'),
    path('api_radio', api_radio ,name= 'api_radio'),
    path('api_radio_tracks/<slug:slug>', api_radio_tracks ,name= 'api_radio_tracks'),
    path('login', LoginView.as_view(), name = 'login'),
    path('register', RegisterView.as_view(), name= 'register'),
    path('like_song/<slug:slug>', LikeSong.as_view(), name='like_song')
]
# http://127.0.0.1:8000/api_radio_tracks/37151

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)