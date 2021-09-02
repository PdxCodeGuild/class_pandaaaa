from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Post(models.Model):
    title = CharField(max_length=200)
    author = CharField(max_length=60)
    body = CharField(max_length=200000)
    