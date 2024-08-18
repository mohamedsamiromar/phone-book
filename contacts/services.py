from contacts.models import Contact, PhoneNumber
from account.models import User


class CreateConect:

    @staticmethod
    def create_contact(
        user: User,
        name: str,
        phone_numbers: list[str],
        address: str = None,
        is_favorite: bool = False
    ) -> Contact:
  
        contact = Contact.objects.create(
            user=user,
            name = name,
            address = address,
            is_favorite = is_favorite
            )

        for phone_num in phone_numbers:
            phone_number = PhoneNumber.objects.create(
                contact= contact,
                phone_number = phone_num
            )

        return contact
        