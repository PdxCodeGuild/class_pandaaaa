from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200, default="J Doe")
    phone_number= PhoneNumberField()
    address= models.CharField(max_length=200, default="address")
    email= models.EmailField(max_length=254)
    def __str__(self):
      return self.name


