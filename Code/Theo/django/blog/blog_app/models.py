from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=CASCADE,related_name='posts')
    public = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title