from django.db import models

# Create your models here.
class Movie(models.Model):
    class Rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    
    title = models.CharField(max_length=50, blank=True, null=True)
    starRating = models.IntegerField(choices=Rating.choices)
    def __str__(self):
        return self.title

class Villain(models.Model):
    name = models.CharField(max_length=50)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, null=True, blank=True, related_name='Movie')
    image = models.CharField(max_length=400, null=True, blank=True)
    def __str__(self):
        return self.name
