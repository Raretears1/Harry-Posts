from django import forms

from hackerposts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author_name", "text"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author_name", "text"]