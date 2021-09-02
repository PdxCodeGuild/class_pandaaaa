from django.contrib import admin
from .models import Artist, Album, Playlist, Song, UserProfile
# Register your models here.

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(UserProfile)