from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, \
    CreateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, FavoritePosts
from .serializers import PostSerializer, FavoritePostSerializer


class PostAddView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        post = {
            "user": request.user.id,
            "title": request.data.get("title"),
            "text": request.data.get("text")
        }
        post_data = PostSerializer(data=post)
        if post_data.is_valid(raise_exception=True):
            post_data.save()

        return Response(post, status=status.HTTP_201_CREATED)


class PostListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.order_by('-created', status=status.HTTP_200_OK)


class FavoritePostCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if FavoritePosts.objects.filter(post=request.data.get("post"), user=request.user.id).exists():
            raise ValidationError("Post already flagged by this user")
        post = {
            "user": request.user.id,
            "post": request.data.get("post"),
            "flagged_post": request.data.get("flagged_post")
        }
        post_data = FavoritePostSerializer(data=post)
        if post_data.is_valid(raise_exception=True):
            post_data.save()
            return Response(post, status=status.HTTP_201_CREATED)
        else:
            Response(status=status.HTTP_400_BAD_REQUEST)


class FavoritePostUpdateView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    model = FavoritePosts
    serializer_class = FavoritePostSerializer

    def get_object(self):
        return self.model.objects.get(user=self.request.user.id, post= self.request.data.get("post"))

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        post = {
            "flagged_post": request.data.get("flagged_post")
        }
        patch_data = self.get_serializer(instance, data=post, partial=True)
        if not patch_data.is_valid():
            return Response({"message": "failed", "details": patch_data.errors})
        patch_data.save()
        return Response(patch_data.data, status=status.HTTP_200_OK)
