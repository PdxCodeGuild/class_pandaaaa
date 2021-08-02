from django import forms
from django.forms import widgets
from .models import Priority,ToDoItem

class ToDoForm(forms.ModelForm):
    class Meta:    
        model= ToDoItem
        fields= ['text','priority']
        widgets = {
            'priority' : widgets.RadioSelect()
        }