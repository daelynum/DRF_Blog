from django.contrib import admin

from postapp.models import Post, ReadPosts, FavoriteUsers


class AdminPost(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'user')


class AdminReadPost(admin.ModelAdmin):
    list_display = ('user', 'post', 'read')


class AdminFavoriteUser(admin.ModelAdmin):
    list_display = ('main_user', 'secondary_user')

admin.site.register(Post, AdminPost)
admin.site.register(ReadPosts, AdminReadPost)
admin.site.register(FavoriteUsers, AdminFavoriteUser)
