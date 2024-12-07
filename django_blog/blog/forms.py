from django import forms
from .models import Post
from taggit.forms import TagWidget  # Import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Ensure 'tags' field is included
        widgets = {
            'tags': TagWidget(),  # Use TagWidget for the tags field
        }
