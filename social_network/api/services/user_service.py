from ..models import User

from django.utils.timezone import now

from rest_framework import exceptions


class UserService:

    @staticmethod
    def get_all_users() -> list:
        return User.objects.all()

    @staticmethod
    def create_user(user_data: dict) -> User:
        instance = User(username=user_data["username"])
        instance.set_password(user_data["password"])
        instance.save()

        return instance

    @staticmethod
    def get_user_by_username(username: str) -> User:
        user = User.objects.get(username=username)
        if user is None:
            raise exceptions.NotFound()
        return user

    @staticmethod
    def update_last_user_request_date(user: User) -> None:
        User.objects.filter(pk=user.pk).update(last_request=now())
