from rest_framework import serializers


class LikesPerDateAnalyticsSerializer(serializers.Serializer):
    date = serializers.CharField()
    likes_count = serializers.IntegerField()
