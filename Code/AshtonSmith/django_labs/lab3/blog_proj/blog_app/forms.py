from django.forms.forms import Form
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'public']

      