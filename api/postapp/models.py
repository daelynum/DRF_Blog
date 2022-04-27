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


@receiver(post_save, sender=Post)
def add_num_of_posts(sender, instance, **kwargs):
    user = instance.user
    user.count_of_posts += 1
    user.save()


class ReadPosts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)
    read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Read post'
        verbose_name_plural = 'Read posts'

    def __str__(self):
        return self.user


class FavoritePosts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)
    flagged_post = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Favorite post'
        verbose_name_plural = 'Favorite posts'

    def __str__(self):
        return self.id
