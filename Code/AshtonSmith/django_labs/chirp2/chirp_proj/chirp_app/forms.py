from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Post, Comment

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password')

class PostForm(forms.ModelForm):
    # text = forms.CharField(widget=forms.Textarea, label='')
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'HELLO?'}))
    class Meta:
        model = Post
        fields = ('text',)
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'dj-form'})



class CommentForm(forms.ModelForm):
    # text = forms.CharField(widget=forms.Textarea, label='')
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Chirp a Reply?'}))
    class Meta:
        model = Comment
        fields = ('text',)
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'comment-form'})

