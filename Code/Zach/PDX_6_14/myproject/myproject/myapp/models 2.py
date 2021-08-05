from django.db import models

class MyModel(models.Model): 
    numbers = models.IntegerField(default=0)   
    def __str__(self):
        return self.numbers
