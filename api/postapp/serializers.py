from rest_framework import serializers
from .models import Post, ReadPosts


class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ['id', 'created', 'title', 'text', 'user']


class ReadPostsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ReadPosts
        fields = '__all__'


class PostsFavUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['created', 'title', 'text', 'user_id']
