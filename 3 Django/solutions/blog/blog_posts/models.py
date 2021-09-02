from typing import Text
from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth import get_user_model

class Tag(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = CharField(max_length=200)
    body = TextField()
    user = ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    date_created = DateTimeField(auto_now_add=True)
    date_edited = DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.title
