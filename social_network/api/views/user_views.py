from ..services import UserService

from ..serializers.user_serializers import UserSerializer
from ..serializers.user_serializers import UserActivitySerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED
)

from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_yasg.utils import swagger_auto_schema


class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            HTTP_200_OK: UserSerializer(many=True),
            HTTP_401_UNAUTHORIZED: ""
        }
    )
    def get(self, request):
        users = UserService.get_all_users()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserActivityView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            HTTP_200_OK: UserActivitySerializer(many=True)
        }
    )
    def get(self, request):
        user = request.user
        serializer = UserActivitySerializer(user)
        return Response(serializer.data)
