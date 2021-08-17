from django import forms
from django.forms import widgets
from .models import TodoModel



class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
# date = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

class TodoForm(forms.ModelForm):

    class Meta:
        model = TodoModel
        fields = ['title', 'details','startdate','starttime','duedate','duetime','priority',]

        widgets = {
            'startdate': DateInput(),
            'duedate': DateInput(),
            'starttime': TimeInput(),
            'duetime': TimeInput(),
        }
                
        
        
        
        
        # widgets = {
        #     'startdate':forms.DateField(widget=widgets.SelectDateWidget(empty_label="Nothing")),
        #     'duedate':forms.DateField(widget=widgets.SelectDateWidget(empty_label="Nothing")),
        # }
        # field1 = forms.DateField(
        # # fields = '__all__'



        
    #     title = models.CharField(max_length=200)
    # details = models.CharField(max_length=500)
    # startdate = models.DateTimeField()
    # duedate = models.DateTimeField()
    # completed = models.BooleanField(False)
    # priority = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)