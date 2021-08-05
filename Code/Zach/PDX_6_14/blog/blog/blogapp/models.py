from django.db import models
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth import get_user_model

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=200)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    public = models.BooleanField(max_length=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title