from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=256, null=True)
    last_name = models.CharField(max_length=256, null=True)
    cohort = models.CharField(max_length=256, null=True)
    fav_topic = models.CharField(max_length=256, null=True, blank=True)
    fav_teacher = models.CharField(max_length=256, null=True, blank=True)
    capstone = models.URLField(max_length=256, null=True, blank=True)

    def __str__(self) -> str:
        return self.first_name + ' ' +self.last_name

    
