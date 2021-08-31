from django.db import models


class Student(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=500)
    cohort = models.CharField(max_length=500)
    favoriteTopic = models.CharField(max_length=500)
    favoriteTeacher = models.CharField(max_length=500)
    capstone = models.URLField()

    def __str__(self):
        return self.firstName + " " + self.lastName
