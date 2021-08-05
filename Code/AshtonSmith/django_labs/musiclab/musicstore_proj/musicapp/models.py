from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models.deletion import CASCADE
# Create your models here.

class Song(models.Model):
    name = CharField(max_length=200)
    # album = ForeignKey(Album, on_delete=CASCADE, related_name='song')
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
    def __str__(self):
        return self.name



