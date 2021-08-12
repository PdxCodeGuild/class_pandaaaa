from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.
#models.py
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    avatar = models.ImageField()