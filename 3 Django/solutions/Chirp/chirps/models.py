from django.db import models
from accounts.models import CustomUser

class Chirp(models.Model):
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='chirps')
    chirp = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.created)


