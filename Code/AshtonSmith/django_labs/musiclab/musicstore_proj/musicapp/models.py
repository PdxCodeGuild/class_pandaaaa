from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models.deletion import CASCADE
from django.core.validators import int_list_validator
from django.contrib.auth.models import User
# Create your models here.

class Song(models.Model):
    name = CharField(max_length=200)
    # album = ForeignKey('Album', on_delete=CASCADE, related_name='song')
    def __str__(self):
       return self.name

class Artist(models.Model):
    name = CharField(max_length=200)
    def __str__(self):
       return self.name

class Album(models.Model):
    genre_list = (('rock','rock'),('pop','pop'),('rap','rap'))
    name = CharField(max_length=200)
    genre = CharField(max_length=200,choices=genre_list,default='rock')
    songs = ManyToManyField(Song, related_name='album')
    artist = ForeignKey(Artist, on_delete=CASCADE,related_name='album')
    cover_art = models.ImageField(default=None, null=True)
    def __str__(self):
        return self.name

class Playlist(models.Model):
    name = CharField(max_length=200)
    song_list = models.CharField(validators=[int_list_validator], max_length=100)
    def __str__(self):
        return self.song_list

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    avatar = models.ImageField()
    liked_songs = models.ForeignKey(Playlist, on_delete=CASCADE, related_name='userprofile')
    last_activity = models.DateTimeField()






