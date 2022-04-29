
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
            raise ValidationError("Post already flagged by this user as readed, use PATCH method")
        return self.create(request, *args, **kwargs)


class ReadPostsUpdateView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    model = ReadPosts
    serializer_class = ReadPostsSerializer

    def get_object(self):
        return self.model.objects.get(user=self.request.user.id, post=self.request.data.get("post"))

    def patch(self, request, *args, **kwargs):
        if ReadPosts.objects.filter(post=request.data.get("post"),
                                    user=request.user.id,
                                    flagged_post=request.data.get('flagged_post')).exists():
            raise ValidationError(f"Post already flagged {request.data.get('flagged_post')} by this user")
        return self.partial_update(request, *args, **kwargs)


class PostListAuthorizedView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostsFavUserSerializer
    pagination_class = MyOffsetPagination

    def get_queryset(self):
        id_nums = [
            i.secondary_user_id
            for i in FavoriteUsers.objects.filter(
                main_user=self.request.user.id, favorite_user=True
            ).iterator()
        ]

        result = []
        for id in id_nums:
            for i in Post.objects.filter(user_id=id).order_by('-created'):
                result.append(i)
        return result


"""prefetched_related подтягивает обьекты из др таблицы (сделать везде в get запросах)
{'favorite_user': 'False', 'secondary_user': 'user1@user.user', 'main_user': 'vladimir@mail.ru'}"""
# return FavoriteUsers.objects.filter(main_user=self.request.user.id).select_related('main_user')


# posts = Post.objects.all().filter(user=self.request.user.id).values_list('created', 'title', 'text')
# fav_users = FavoriteUsers.objects.filter(main_user=self.request.user.id).values_list('main_user', 'secondary_user', 'favorite_user')
# return posts | fav_users
