from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveAPIView, FavoriteUserView, FavoriteUserUpdateView

app_name = 'authapp'
urlpatterns = [
    path('user/', RegistrationAPIView.as_view(), name='user'),
    path('user/login/', LoginAPIView.as_view(), name='login'),
    path('users/', UserRetrieveAPIView.as_view(), name='users'),
    path('users/favorite_user/', FavoriteUserView.as_view(), name='favorite_user'),
    path('users/favorite_user/update/', FavoriteUserUpdateView.as_view(), name='favorite_user_update'),
]