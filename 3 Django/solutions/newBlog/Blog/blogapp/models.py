from django.db import models
from django.db.models.fields import BooleanField, CharField, DateField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth import get_user_model

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='blog')
    date_created = models.DateField(auto_now_add=True)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.title


