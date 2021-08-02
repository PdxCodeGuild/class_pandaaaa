from django.db import models

# Create your models here.
class Shortened_Url(models.Model):
    code = models.CharField(max_length=12)
    url = models.URLField(max_length=256)
    counter = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.url
