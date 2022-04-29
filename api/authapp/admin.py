from django.contrib import admin

from authapp.models import User


class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff', 'created_at', 'count_of_posts')


class AdminFavoriteUser(admin.ModelAdmin):
    list_display = ('main_user', 'secondary_user')


admin.site.register(User, AdminUser)
# admin.site.register(FavoriteUsers, AdminFavoriteUser)
