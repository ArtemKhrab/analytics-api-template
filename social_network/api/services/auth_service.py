from ..models import User

from django.utils.timezone import now

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import exceptions


class AuthService:
    @staticmethod
    def create_token(user):
        token = RefreshToken.for_user(user)
        User.objects.filter(pk=user.pk).update(last_login=now())
        return {
            "access": token.access_token,
            "refresh": token,
        }

    @staticmethod
    def login(user, login_data):
        if not user.check_password(login_data["password"]):
            raise exceptions.AuthenticationFailed()
        return AuthService.create_token(user)
