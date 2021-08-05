
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField, IntegerField
from django.utils import timezone
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body= models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='posts')
    public = models.BooleanField(default=True)
    date_created = DateTimeField(auto_now_add=True)
    date_edited = DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    #  fields = ['title', 'body', 'public', 'date_created','date_edited',]




# class Priority(models.Model):
#     PRIORITY = {
#         ('high', 'HIGH'),
#         ('medium', 'MEDIUM'),
#         ('low', 'LOW'),
#     }
#     choice = models.CharField(max_length=7,blank = True, choices=PRIORITY,default='HIGH')
#     def __str__(self):
#         return self.choice 

# class TodoModel(models.Model):
#     title = models.CharField(max_length=200)
#     details = models.CharField(max_length=500)
#     startdate = models.DateField(default=timezone.now)
#     starttime = models.TimeField(default=timezone.now)
#     duedate = models.DateField(default=timezone.now)
#     duetime = models.TimeField(default=timezone.now)
#     completed = models.BooleanField(default=False)
#     priority = models.ForeignKey(Priority, on_delete=CASCADE)

#     def __str__(self):
#         return self.title
