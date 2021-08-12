from django.db import models

# Create your models here.

from django.db import models

class my_ari_model(models.Model):
    myfield = models.CharField(max_length=500)
    
    def __str__(self):
        return self.myfield