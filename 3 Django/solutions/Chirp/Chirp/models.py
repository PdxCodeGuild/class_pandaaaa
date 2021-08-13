from django.db import models
from users.models import CustomUser

# Create your models here.

class Chirp(models.Model):
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='chirps', null=True)
    message = models.CharField(max_length=128)
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.posted)