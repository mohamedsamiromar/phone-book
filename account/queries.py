from . models import User


def get_user_by_username(username: str) -> User:
        return User.objects.filter(username=username).exists()


def get_user_by_email(email: str) -> User:
        return User.objects.filter(email=email).exists()
