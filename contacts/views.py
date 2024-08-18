from rest_framework import viewsets
from account.models import User
from contacts.serializers import CreateContactSerializer, ContactSerializer
from contacts.models import Contact
from rest_framework.response import Response
from rest_framework import status
from contacts.services import CreateConect


class ContactView(viewsets.ViewSet):

    def create(self, request):
        serializer = CreateContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(email=request.user)
        instance = CreateConect.create_contact(user=user, **serializer.validated_data)
        serializer = ContactSerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def list(self, request):
        contacts = Contact.objects.filter(user=request.user)
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)