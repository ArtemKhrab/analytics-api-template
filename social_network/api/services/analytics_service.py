from ..models import Like

from django.db.models import Count
from django.db.models.functions import TruncDay


class AnalyticsService:
    @staticmethod
    def get_likes_per_day_analytics(date_from, date_to):
        likes = Like.objects.filter(date_created__date__range=[date_from, date_to])
        likes_per_day = likes.annotate(date=TruncDay('date_created')).values('date').annotate(
            likes_count=Count('id')).order_by('date')
        return likes_per_day
