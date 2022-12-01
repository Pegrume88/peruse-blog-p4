from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'featured_image',)

        widgets = {
            'title': forms.TextInput({'class': 'form-control'}),
            'author': forms.Select({'class': 'form-control'}),
            'content': forms.Textarea({'class': 'form-control'}),
            'featured_image': forms.FileInput({'class': 'form-control-file'}),

        }
