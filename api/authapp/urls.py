from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveAPIView

app_name = 'authapp'
urlpatterns = [
    path('user/', RegistrationAPIView.as_view(), name='user'),
    path('user/login/', LoginAPIView.as_view(), name='login'),
    path('users/', UserRetrieveAPIView.as_view(), name='users'),
]