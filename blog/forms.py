from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """PostForm definition."""

    class Meta:
        model=Post
        fields=['title','body','category','seo_title','seo_description','status']
