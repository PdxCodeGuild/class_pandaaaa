from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Task(models.Model):
    task_title = models.CharField(max_length=200)
    task_detail = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    date_completed = models.DateTimeField(null=True, blank=True)
    complete = models.BooleanField()

    def __str__(self):
        return self.task_title