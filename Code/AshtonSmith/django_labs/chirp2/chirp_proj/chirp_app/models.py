from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE
from django.utils.timezone import now


# Create your models here.
class Comment(models.Model):
    text = CharField(max_length=200)
    posttime = models.TimeField(default=now())
    postdate = models.DateField(default=now())
    author = ForeignKey('CustomUser',on_delete=CASCADE,related_name='comment_author',null=True)
    post = ForeignKey('Post',on_delete=CASCADE,related_name='post_comment',null=True)
    def __str__(self):
        return self.text

class CustomUser(AbstractUser):
    userposts = CharField(max_length=500)
    joindate = models.DateField(default=now())
    avatar = models.ImageField(default=None)
    post_count = models.IntegerField(default=0)
    def __str__(self):
        return self.username

class Post(models.Model):
    text = CharField(max_length=200)
    author = ForeignKey(CustomUser,on_delete=CASCADE,related_name='post_author',null=True)
    posttime = models.TimeField(default=now())
    postdate = models.DateField(default=now())
    comment_count = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.text