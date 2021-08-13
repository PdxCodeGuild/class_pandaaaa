from django.forms import ModelForm, Textarea

from .models import Cheep

class CheepForm(ModelForm):
    class Meta:
        model = Cheep
        fields = ['message']

        widgets = {
            'message': Textarea(attrs={
                'rows': 4,
                'maxlength': Cheep.MAX_LENGTH,
                'name' : 'Cheep',
                }),
            # 'user': HiddenInput(),
        }