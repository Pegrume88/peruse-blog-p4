from .models import Comment, Post
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ('title', 'category', 'author', 'content', 'featured_image', 'status')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control-file'}),

        }
