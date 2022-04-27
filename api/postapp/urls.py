from django.urls import path

from .views import PostAddView, PostListView, FavoritePostCreateView, FavoritePostUpdateView

app_name = 'postapp'
urlpatterns = [
    path('add/', PostAddView.as_view()),
    path('all/', PostListView.as_view()),
    path('flagged_post/', FavoritePostCreateView.as_view()),
    path('flagged_post_update/', FavoritePostUpdateView.as_view()),
]
