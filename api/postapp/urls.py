from django.urls import path

from .views import PostAddView, PostListUnauthorizedView, ReadPostsCreateView, ReadPostsUpdateView, PostListAuthorizedView

app_name = 'postapp'
urlpatterns = [
    path('add/', PostAddView.as_view()),
    path('all/', PostListUnauthorizedView.as_view()),
    path('readed_post/', ReadPostsCreateView.as_view()),
    path('readed_post_update/', ReadPostsUpdateView.as_view()),
    path('posts_from_fav_users/', PostListAuthorizedView.as_view()),
]
