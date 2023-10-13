from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from . service import *


class AuthSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return AccountService.optain_access_token(
            user=user,
            group=GroupEnum.PERSON,
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