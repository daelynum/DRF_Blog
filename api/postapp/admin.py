from django.contrib import admin

from postapp.models import Post, ReadPosts


class AdminPost(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'user')


class AdminReadPost(admin.ModelAdmin):
    list_display = ('user', 'post', 'flagged_post')


admin.site.register(Post, AdminPost)
admin.site.register(ReadPosts, AdminReadPost)
