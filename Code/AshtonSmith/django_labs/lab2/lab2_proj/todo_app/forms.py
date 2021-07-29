from django import forms
from django.forms import widgets
from .models import TodoModel

class TodoForm(forms.ModelForm):

    class Meta:
        model = TodoModel
        fields = ['title', 'details','startdate','duedate','priority']
        widgets = {
            'startdate':widgets.DateTimeInput(),
            'duedate':widgets.DateInput(),
        }
        # fields = '__all__'



        
    #     title = models.CharField(max_length=200)
    # details = models.CharField(max_length=500)
    # startdate = models.DateTimeField()
    # duedate = models.DateTimeField()
    # completed = models.BooleanField(False)
    # priority = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)