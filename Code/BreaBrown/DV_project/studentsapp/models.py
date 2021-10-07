from django.db import models
# from django.db.models.fields import CharField, URLField
from django.db.models import CharField, URLField

class Students(models.Model):
    fname = CharField(max_length=50)
    lname = CharField(max_length=50)
    Cohort = CharField(max_length=100)
    fav_topic = CharField(max_length=100)
    fav_teacher = CharField(max_length=100)
    Capstone = URLField(max_length=250)
    
    def __str__(self) -> str:
        return self.fname