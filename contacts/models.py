from django.db import models
from account.models import BaseModel, User


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_contact', null=True)
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=15, null=True)

    def __str__(self) -> str:
        return f"{self.contact}_{self.phone_number}"