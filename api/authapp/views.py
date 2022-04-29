from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, FavoriteUsers
from .renderers import UserJSONRenderer
from .serializers import RegistrationSerializer, LoginSerializer, UserInfoSerializer, \
    FavoriteUserSerializer


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveAPIView(ListAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = User.objects.all()
        count_of_posts = self.request.query_params.get('count_of_posts', None)
        if count_of_posts is not None:
            queryset = User.objects.order_by('-count_of_posts')
        return queryset


class FavoriteUserView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FavoriteUserSerializer

    def post(self, request, *args, **kwargs):
        if FavoriteUsers.objects.filter(secondary_user=request.data.get("secondary_user"),
                                        favorite_user=request.data.get('favorite_user')).exists():
            raise ValidationError("This user already flagged as favorite, if you want to change it use PATCH method")
        return self.create(request, *args, **kwargs)


class FavoriteUserUpdateView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    model = FavoriteUsers
    serializer_class = FavoriteUserSerializer

    def get_object(self):
        return self.model.objects.get(main_user=self.request.user.id,
                                      secondary_user=self.request.data.get("secondary_user"))

    def patch(self, request, *args, **kwargs):
        if FavoriteUsers.objects.filter(secondary_user=request.data.get("main_user"),
                                        favorite_user=request.data.get('favorite_user')).exists():
            raise ValidationError(f"User already flagged {request.data.get('favorite_user')} by this user")
        return self.partial_update(request, *args, **kwargs)
