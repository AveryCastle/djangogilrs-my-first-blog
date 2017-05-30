from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text',]
        #exclude = ['author', 'created_date', 'published_date'] 
