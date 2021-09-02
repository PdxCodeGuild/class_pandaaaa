from django.db import models
from django.db.models.fields import CharField
# from django.forms import widgets
from django.utils import timezone
import json

# Create your models here.
class Priority(models.Model):
    PRIORITY_CHOICES = (
        ('High','HIGH'),
        ('Medium','MEDIUM'),
        ('Low','LOW'),
    )
    name = models.CharField(max_length=256, choices=PRIORITY_CHOICES, default='HIGH')
    def __str__(self) -> str:
        return self.name

class ToDoItem(models.Model):
    text = models.CharField(max_length=256)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE,null=True,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(auto_now_add=False, null=True)
    def __str__(self) -> str:
        return self.text


