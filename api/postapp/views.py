from rest_framework.generics import ListCreateAPIView
from .models import Post


class PostAddView(ListCreateAPIView):
    queryset = Post.objects.all
