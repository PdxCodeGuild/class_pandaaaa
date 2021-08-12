from django.forms import ModelForm, widgets
from .models import CustomUser

class ProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar','about']

        widgets = {
            'avatar': widgets.ClearableFileInput()
        }