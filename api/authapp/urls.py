from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveAPIView

app_name = 'authapp'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('user/', UserRetrieveAPIView.as_view()),
]