
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import HomeView, AlbumView, ArtistView, SongView
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('home/',HomeView.as_view() ,name= 'home' ),
    path('album/<slug:pk>',AlbumView.as_view() ,name= 'album' ),
    path('song/<slug:pk>',SongView.as_view() ,name= 'song' ),
    path('artist/<slug:pk>',ArtistView.as_view() ,name= 'artist' ),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)