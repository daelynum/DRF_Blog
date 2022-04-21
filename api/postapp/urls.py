from django.urls import path

from .views import PostAddView

app_name = 'authapp'
urlpatterns = [
    path('add/', PostAddView.as_view()),
]