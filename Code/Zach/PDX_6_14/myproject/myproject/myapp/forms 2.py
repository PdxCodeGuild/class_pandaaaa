from django import forms
from .models import MyModel
class NumForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ("numbers",)