from datetime import datetime

from ..services import AnalyticsService
from ..serializers.analytics_serializers import LikesPerDateAnalyticsSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED,
    HTTP_400_BAD_REQUEST
)

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class LikesAnalyticsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('date_from', openapi.IN_QUERY,
                              type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
            openapi.Parameter('date_to', openapi.IN_QUERY,
                              type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
        ],
        responses={
            HTTP_200_OK: LikesPerDateAnalyticsSerializer(many=True),
            HTTP_401_UNAUTHORIZED: "",
            HTTP_400_BAD_REQUEST: ""
        }
    )
    def get(self, request):
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')
        if not date_to or not date_to:
            return Response(
                data={"detail": "Date_from and date_to params are mandatory."},
                status=HTTP_400_BAD_REQUEST
            )

        try:
            date_from = datetime.fromisoformat(date_from)
            date_to = datetime.fromisoformat(date_to)
        except ValueError:
            return Response(
                data={"detail": "Invalid date format. Use YYYY-MM-DD."},
                status=HTTP_400_BAD_REQUEST
            )

        aggregated_data = AnalyticsService.get_likes_per_day_analytics(
            date_from=date_from,
            date_to=date_to
        )
        serializer = LikesPerDateAnalyticsSerializer(aggregated_data, many=True)
        return Response(serializer.data)
