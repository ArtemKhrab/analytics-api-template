from ..models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.password_validation import validate_password


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        required=True
    )
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password],
        required=True
    )

    class Meta:
        model = User
        fields = ("username", "password")
        extra_kwargs = {"password": {"write_only": True}}
