from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer


class PostAddView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        all_posts = Post.objects.all()
        serialized_posts = PostSerializer(all_posts, many=True)

        return Response({"posts": serialized_posts.data}, status=status.HTTP_200_OK)

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
