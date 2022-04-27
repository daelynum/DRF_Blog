from rest_framework import serializers
from .models import Post, FavoritePosts


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'created', 'title', 'text', 'user']


class FavoritePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritePosts
        fields = '__all__'
