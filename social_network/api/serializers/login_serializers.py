from ..models import User

from rest_framework import serializers


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True
    )
    password = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = ("username", "password")
        extra_kwargs = {"password": {"write_only": True}}
