from django.db import models
from django.conf import settings
from django.db.models.fields import IntegerField
from django.utils import timezone

class TodoModel(models.Model):
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=500)
    startdate = models.DateTimeField(default=timezone.now)
    duedate = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField()
    def __str__(self):
        return self.title