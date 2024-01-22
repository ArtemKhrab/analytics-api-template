from ..models import Post
from ..models import Like

from rest_framework import serializers


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("text",)


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("id", "text", "likes_count", "date_created")
        read_only_fields = ("id", "likes_count", "date_created")

    @staticmethod
    def get_likes_count(obj):
        return Like.objects.filter(post=obj).count()
