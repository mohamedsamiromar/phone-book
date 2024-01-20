from account import queries
from .models import LoginLog, User
from contacts.models import Contact
from core.errors import Error, APIError


class AccountService:
    def Login_obtain_access_token(user: User, token: dict) -> dict:
        if user.is_blocked:
            raise APIError(Error.BLOCKED_USER)
        else:
            return token

    @staticmethod
    def login(username: str) -> None:
        LoginLog.objects.create(username=username)



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
            
            if queries.get_user_by_username(username=username):
                raise APIError(Error.USERNAME_ALREADY_EXIST)
            if queries.get_user_by_email(email=email):
                raise APIError(Error.EMAIL_ALREADY_EXIST)
            
            user = User(
                email=email,
                first_name= first_name,
                middle_name= middle_name,
                last_name= last_name,
                birth_date= birth_date,
                username= username,
            )

            user.set_password(password)
            user.save()
            return user
