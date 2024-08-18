from rest_framework import serializers
from . models import Contact


class CreateContactSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone_numbers = serializers.ListField(child=serializers.CharField())
    address = serializers.CharField(required=False)
    is_favorite = serializers.BooleanField(required=False)



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'