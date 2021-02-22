from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import View

from hackerposts.forms import PostForm
from hackerposts.models import Post
from django.shortcuts import render, get_object_or_404, redirect


class PostsListView(ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"


class PostCreateView(CreateView):
    template_name = "post_form.html"
    model = Post
    fields = ('author_name', 'text')


class PostCreateComment(CreateView):
    template_name = "post.html"
    model = Post
    fields = ('author_name', 'text')
