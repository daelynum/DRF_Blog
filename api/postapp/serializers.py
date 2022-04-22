from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'created', 'title', 'text', 'user']

    # def create(self, validated_data):
    #     return Post.objects.create(**validated_data)

