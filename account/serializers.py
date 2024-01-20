from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from . service import *


class AuthSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        print(user.id)
        token = super().get_token(user)
        return AccountService.Login_obtain_access_token(
            user=user,
            token=token
        )


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    middle_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()
    birth_date = serializers.DateField()
    password = serializers.CharField()



class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'