from rest_framework import serializers
from . models import Contact


class CreateContactSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone_number1 = serializers.CharField()
    phone_number2 = serializers.CharField(required=False)
    telephone = serializers.CharField(required=False)
    email =serializers.EmailField(required=False)
    address = serializers.CharField(required=False)
    is_favorite = serializers.BooleanField(required=False)



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'