import psycopg2
from django.db import connection
from django.db.models import OuterRef, Subquery
from psycopg2.extras import RealDictCursor
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from authapp.models import FavoriteUsers
from .models import Post, ReadPosts
from .paginations import MyOffsetPagination
from .serializers import PostSerializer, ReadPostsSerializer, PostsFavUserSerializer


class PostAddView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer


class PostListUnauthorizedView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.order_by('-created')


class ReadPostsCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReadPostsSerializer

    def post(self, request, *args, **kwargs):
        if ReadPosts.objects.filter(post=request.data.get("post"), user=request.user.id).exists():
            raise ValidationError("Post already flagged by this user as readed")
        return self.create(request, *args, **kwargs)


class PostListSubscriptionView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostsFavUserSerializer
    pagination_class = MyOffsetPagination

    def get_queryset(self):
        conn = psycopg2.connect('dbname=api')
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            """
            SELECT created, title, text, user_id
            FROM postapp_post
            WHERE user_id IN (
                SELECT secondary_user_id
                FROM authapp_favoriteusers
                WHERE main_user_id = %s
                )
                ORDER BY created DESC"""
            , [self.request.user.id])
        return cursor.fetchall()


class PostListAuthorizedView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        read_posts = self.request.query_params.get('read_posts', None)
        if read_posts is not None:
            conn = psycopg2.connect('dbname=api')
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute(
                """
                SELECT created, title, text, user_id
                FROM postapp_post
                WHERE id IN (
                    SELECT post_id
                    FROM postapp_readposts
                    WHERE user_id = %s
                    ) """
                , [self.request.user.id])
            return cursor.fetchall()
        return Post.objects.all()
