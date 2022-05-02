from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from authapp.models import User


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    text = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['created']

    def __str__(self):
        return self.title


class ReadPosts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)
    flagged_post = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Read post'
        verbose_name_plural = 'Read posts'

    def __str__(self):
        return f'{self.user} | {self.post}'
