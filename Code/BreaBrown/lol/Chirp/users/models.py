from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # slogan = models.CharField(max_length=100)
    pass

    def __str__(self):
        return self.username