from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import widgets
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password1','password2','email']
        widgets = {
            'password': widgets.PasswordInput()
        }

class ProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        readonly_fields = ['username']
        fields = ['password']
        widgets = {
            'password': widgets.PasswordInput()
        }