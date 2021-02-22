from django.db import models
from django.urls import reverse


class Post(models.Model):
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='publication date')

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")

    author_name = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='publication date')

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('comment', kwargs={'pk': self.pk})
