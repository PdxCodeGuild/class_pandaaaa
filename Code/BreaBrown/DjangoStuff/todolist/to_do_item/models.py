from django.db import models

# Create your models here.

class Priority(models.Model):
    CHOICE = (('low', 'LOW'), ('medium', 'MEDIUM'), ('high','HIGH'))
    status = models.CharField(max_length = 20, blank = True, choices = CHOICE)
    def __str__(self):
        return self.status

class Task(models.Model):
    title = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    completion_status = models.BooleanField(default=True)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    def __str__(self):
            return self.title