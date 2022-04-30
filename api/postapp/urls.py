from django.urls import path

from .views import PostAddView, PostListUnauthorizedView, ReadPostsCreateView, PostListSubscriptionView, PostListAuthorizedView

app_name = 'postapp'
urlpatterns = [
    path('add/', PostAddView.as_view()),
    path('all/', PostListUnauthorizedView.as_view()),
    path('flag_post_as_readed/', ReadPostsCreateView.as_view()),
    path('posts_from_fav_users/', PostListSubscriptionView.as_view()),
    path('readed_posts/', PostListAuthorizedView.as_view()),
]
