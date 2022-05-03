from django.db.models.signals import post_save
from django.dispatch import receiver

from postapp.models import Post


@receiver(post_save, sender=Post)
def add_num_of_posts(sender, instance, **kwargs):
    user = instance.user
    user.count_of_posts += 1
    user.save()