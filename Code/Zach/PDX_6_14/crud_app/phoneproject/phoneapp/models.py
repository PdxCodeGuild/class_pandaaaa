from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name