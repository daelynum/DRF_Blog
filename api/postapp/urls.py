from django.urls import path

from .views import PostAddView

app_name = 'postapp'
urlpatterns = [
    path('add/', PostAddView.as_view()),
    path('all/', PostAddView.as_view()),
]
