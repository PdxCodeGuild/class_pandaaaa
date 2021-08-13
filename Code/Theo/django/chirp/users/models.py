from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django_countries.fields import CountryField

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    about = models.TextField(max_length=500, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True)
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(50, 50)],
                                      format='JPEG',
                                      options={'quality': 80})
    country = CountryField(null=True,blank=True)

