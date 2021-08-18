from django.db import models
from django.db.models import CharField
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField(max_length=140)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('ChirpApp:detail', args={self.id})

class Meta:
    ordering = ['-date_created']   