from django.contrib import admin

from authapp.models import User


class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff', 'created_at', 'count_of_posts')


admin.site.register(User, AdminUser)
