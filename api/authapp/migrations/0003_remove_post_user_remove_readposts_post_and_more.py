# Generated by Django 4.0.4 on 2022-04-21 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_post_alter_user_options_user_count_of_posts_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='readposts',
            name='post',
        ),
        migrations.RemoveField(
            model_name='readposts',
            name='user',
        ),
        migrations.DeleteModel(
            name='FavoriteUsers',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='ReadPosts',
        ),
    ]
