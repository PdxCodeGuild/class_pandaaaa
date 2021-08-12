from django.db import models
from users.models import CustomUser

# Create your models here.

class Cheep(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='cheeps')
    message = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.created)