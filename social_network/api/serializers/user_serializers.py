from ..models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username",)
        read_only_fields = ("id", "username",)


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "last_login", "last_request")
        read_only_fields = ("id", "last_login", "last_request")
