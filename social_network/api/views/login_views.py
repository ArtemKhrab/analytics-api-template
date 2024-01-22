from ..services import UserService
from ..services import AuthService

from ..serializers.login_serializers import UserLoginSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)

from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from drf_yasg.utils import swagger_auto_schema


class LoginView(APIView):
    @swagger_auto_schema(
        request_body=UserLoginSerializer,
        responses={
            HTTP_200_OK: TokenRefreshSerializer(),
            HTTP_404_NOT_FOUND: "",
            HTTP_400_BAD_REQUEST: "",
        },
    )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login_data = serializer.validated_data

        user = UserService.get_user_by_username(username=login_data["username"])
        token = AuthService.login(user=user, login_data=login_data)

        token_serializer = TokenRefreshSerializer(token)
        return Response(token_serializer.data)
