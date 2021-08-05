
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import HomeView, AlbumView, ArtistView, SongView
urlpatterns = [
    path('home/',HomeView.as_view() ,name= 'home' ),
    path('album/<slug:pk>',AlbumView.as_view() ,name= 'album' ),
    path('song/<slug:pk>',SongView.as_view() ,name= 'song' ),
    path('artist/<slug:pk>',ArtistView.as_view() ,name= 'artist' ),
]
