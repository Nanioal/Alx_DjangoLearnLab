from django import forms
from .models import Post, Comment  # Ensure Comment is imported
from taggit.forms import TagWidget  # Import TagWidget for PostForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Ensure this attribute is included
