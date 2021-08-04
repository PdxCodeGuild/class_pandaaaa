from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from .models import BlogPost

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email']
        widgets = {
            'password': widgets.PasswordInput()
        }

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','body','public']
