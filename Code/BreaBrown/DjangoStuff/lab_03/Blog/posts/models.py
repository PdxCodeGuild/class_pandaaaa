from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('posts:detail', args={self.id})

    class Meta:
        ordering = ['-date_created']
        