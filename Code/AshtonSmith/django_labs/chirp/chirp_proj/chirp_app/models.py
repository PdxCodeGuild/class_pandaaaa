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
    def __str__(self):
        return self.text

class CustomUser(AbstractUser):
    userposts = CharField(max_length=500)
    joindate = models.DateField(default=now())
    avatar = models.ImageField(default=None)
    def __str__(self):
        return self.username

class Post(models.Model):
    text = CharField(max_length=200)
    comments = ForeignKey(Comment,on_delete=CASCADE,related_name='post_comment',null=True)
    author = ForeignKey(CustomUser,on_delete=CASCADE,related_name='post_author',null=True)
    posttime = models.TimeField(default=now())
    def __str__(self):
        return self.text
