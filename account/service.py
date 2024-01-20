from .models import User


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
                email=email,
                first_name= first_name,
                middle_name= middle_name,
                last_name= last_name,
                birth_date= birth_date,
                username= username,
            )

            user.set_password(password)
            user.save()


            print(type(user))
            return user
