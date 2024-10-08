from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework.response import Response
from . service import *
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import status


class LoginAuthView(TokenObtainPairView):

    def post(self, request):
        serializer = AuthSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        AccountService.login(request.data.get('username'))
        return Response(serializer.validated_data)


class RegisterView(viewsets.ViewSet):

    permission_classes = [AllowAny]

    def create(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = RegisterService.register_service(**serializer.validated_data)
        serializer = CreateUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)