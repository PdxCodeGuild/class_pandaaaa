from django.db import models

# Create your models here.

class Cypher(models.Model):
    input_text = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    
    def __str__(self):
        return self.input_text