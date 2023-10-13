from . models import User, LoginLog
from core.errors import Error, APIError
from . models import GroupEnum
from django.contrib.auth.models import Group




class AccountService:

    @staticmethod
    def optain_person_access_token(user: User, token: dict) -> dict:
        if not user.groups.filter(name=GroupEnum.USER.value).exists():
            token['roles'] = list(user.groups.all().values())
            return token

    @staticmethod
    def optain_access_token(group: GroupEnum, user: User, token: dict) -> dict:
        if group == GroupEnum.PERSON:
            return AccountService.optain_person_access_token(
                user=user, token=token)
        else:
            raise APIError(Error.NO_ACTIVE_ACCOUNT)

    @staticmethod
    def login(email: str) -> None:
        LoginLog.objects.create(email=email)



class RegisterService:

    @staticmethod
    def register_service(
        birth_date,
        first_name: str,
        middle_name: str,
        last_name: str,
        email: str,
        password: str,
        username: str
        ) -> User:

        user = User(
            first_name=first_name,
            middle_name = middle_name,
            last_name = last_name,
            email = email,
            birth_date=birth_date,
            username = username
        )
        user.set_password(password)
        user.save()

        group, created = Group.objects.get_or_create(name=GroupEnum.USER.value)
        group.user_set.add(user)

        return user