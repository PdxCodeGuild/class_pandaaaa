from django.db import models

class Priority(models.Model):
    PRIORITY = (
        #left side displayed to user, right side backend info
            ('high', 'HIGH'),
            ('low', 'LOW'), 
            ('medium', 'MEDIUM'),
            )
    name = models.CharField(max_length = 10, choices = PRIORITY, blank = True, default = 'low')
    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField(max_length = 500)
    status = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    completed_at = models.DateTimeField(blank = True, null = True)
    task_duration = models.DecimalField(max_digits = 4, decimal_places = 2, blank = True, null = True)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, null=True, blank=True)
    TODO_TYPE = (
        ('p', 'personal'),
        ('s', 'school'),
        ('w', 'work'),
        ('f', 'family'),
        ('m', 'misc'),
    )
    todo_type = models.CharField(max_length = 1, choices = TODO_TYPE, blank = True, default = 'm')
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', 'created_at']

